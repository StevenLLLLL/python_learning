import sys
import json
import requests
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5 import QtWidgets
from requests_oauthlib import OAuth1
from GUI import Ui_MainWindow  # 导入UI界面
import re  # 用于正则表达式提取数据
from datetime import datetime
import math

search_result = None

current_date = datetime.now().strftime("%Y-%m-%d")
print(current_date)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.foodSearch_Search_PushButton.clicked.connect(self.searchButton_Clicked)
        self.FoodSearch_FoodOuput_ListWidget.itemClicked.connect(self.listWidgetItemClicked)
        self.FoodSearch_AddFood_PushButton.clicked.connect(self.addButton_clicked)
        self.pushButton.clicked.connect(self.todayIn_delete)
        self.selfCheck_Confirm_Pushbutton.clicked.connect(self.selfCheck_Confirm_Pushbutton_clicked)
        self.selfCheck_Output_Label.setText('无')
        self.Metabolism_CaloriesIn_Output.setText('0kcal')
        self.Metabolism_Protein_Output.setText('0克')
        self.Metabolism_Carb_Output.setText('0克')
        self.Metabolism_Fat_Output.setText('0克')
        self.pushButton_2.clicked.connect(self.Metabolism)
        self.pushButton_3.clicked.connect(self.BMI)

        self.calories = 0
        self.carbs = 0
        self.protein = 0
        self.fat = 0
        self.clicked_text = ""

    def BMI(self):
        gender = self.BMI_Gender_ComboBox.currentText()
        weight = self.BMI_Weight_SpinBox.value()
        height = self.BMI_Height_SpinBox.value()
        waist = self.spinBox.value()
        butt = self.spinBox_3.value()
        neck = self.spinBox_4.value()
        health = None
        if waist == 0 or height == 1 or weight == 1 or butt == 0 or neck == 0:
            QMessageBox.warning(self, '提示', '请填写正确的身高/体重/腰围/颈围/臀围')
            return
        BMI = float(weight) / ((float(height) / 100) * (float(height) / 100))
        bodyFat = None
        if gender == '男':
            bodyFat = 86.010 * math.log(waist - neck, 10) - 70.041 * math.log(height, 10) + 36.76
            if 6 <= bodyFat < 14:
                health = '偏瘦'
            elif 18 >= bodyFat >= 14:
                health = '正常'
            elif bodyFat < 6:
                health = '竞技状态'
            elif 25 >= bodyFat > 18:
                health = '偏胖'
            elif 25 < bodyFat:
                health = '过胖'
        elif gender == '女':
            bodyFat = 163.205 * math.log(waist + butt - neck, 10) - 97.684 * math.log(height, 10) - 78.387
            if bodyFat <= 12:
                health = '竞技状态'
            elif 20 >= bodyFat >= 14:
                health = '偏瘦'
            elif 24 >= bodyFat > 20:
                health = '正常'
            elif 31 >= bodyFat > 24:
                health = '偏胖'
            elif 31 < bodyFat:
                health = '过胖'

        self.BMI_Bodyfat_Label_2.setText(f'{round(bodyFat, 2)}%')
        self.label_11.setText(f'{health}')

        self.BMI_Output_Label_2.setText(f'{round(BMI, 2)}')
        if BMI < 18.4:
            self.BMI_Heathness_Label_2.setText('过瘦')
        elif 24 > BMI >= 18.4:
            self.BMI_Heathness_Label_2.setText('正常')
        elif 28 > BMI >= 24:
            self.BMI_Heathness_Label_2.setText('过重')
        elif BMI >= 28:
            self.BMI_Heathness_Label_2.setText('肥胖')

    def selfCheck_Confirm_Pushbutton_clicked(self):
        age = self.selfCheck_Age_spinBox.value()
        weight = self.selfCheck_Weight_spinBox.value()
        height = self.selfCheck_Height_spinBox.value()
        waist = self.selfCheck_Waistline_spinBox.value()
        gender = self.selfCheck_Gender_spinBox.currentText()
        history = self.selfCheck_History_spinBox.currentText()
        BMI = round(float(weight) / (float(height) / 100 * float(height) / 100), 2)
        print('体重指数', BMI)
        score = 0
        if age == 0 or height < 50 or waist <= 10 or weight == 0:
            QMessageBox.warning(self, '提醒', '请输入正确的数据')
            return
        if 34 >= age >= 25:  # 年龄
            score += 4
        elif 39 >= age >= 35:
            score += 8
        elif 44 >= age >= 40:
            score += 11
        elif 45 <= age <= 49:
            score += 12
        elif 50 <= age <= 54:
            score += 13
        elif 55 <= age <= 59:
            score += 15
        elif 55 <= age <= 59:
            score += 16
        elif 64 <= age <= 120:
            score += 18

        if 22 <= BMI < 24:  # BMI指数
            score += 1
        elif 24 <= BMI < 30:
            score += 3
        elif BMI >= 30:
            score += 5

        if gender == '男':  # 腰围
            if 75 <= waist < 80:
                score += 3
            elif 80 <= waist < 85:
                score += 5
            elif 85 <= waist < 90:
                score += 7
            elif 90 <= waist < 95:
                score += 8
            elif 95 <= waist:
                score += 10
        elif gender == '女':
            if 70 <= waist < 75:
                score += 3
            elif 75 <= waist < 80:
                score += 5
            elif 80 <= waist < 85:
                score += 7
            elif 85 <= waist < 90:
                score += 8
            elif 90 <= waist:
                score += 10

        if history == '有':
            score += 6

        if gender == '男':
            score += 2

        if score >= 25:
            self.selfCheck_Output_Label.setText('高风险')

        elif score < 25:
            self.selfCheck_Output_Label.setText('低风险')

    def Metabolism(self):
        try:
            age = self.Metabolism_Age_spinBox.value()
            weight = self.Metabolism_Weight_spinBox.value()
            height = self.Metabolism_Height_spinBox.value()
            move = self.Metabolism_Activity_spinBox.currentText()
            goal = self.Metabolism_WeightGoal_spinBox.value()
            gender = self.comboBox.currentText()
            time = self.spinBox_2.value()
            calories_deficit = ((float(goal) - float(weight)) * 7700) / (time * 30)
            calories = 0
            if gender == '男':
                calories = (10.0 * float(weight) + 6.25 * float(height) - 5.0 * float(age) + 5)
            if gender == '女':
                calories = (10.0 * float(weight) + 6.25 * float(height) - 5.0 * float(age) - 161)
            if move == '整日坐着':
                calories *= 1.2
            elif move == '非常轻（办公室工作&学习）':
                calories *= 1.3
            elif move == '轻度运动（站立工作&行走）':
                calories *= 1.55
            elif move == '中度运动(体力工作&每天运动两小时)':
                calories *= 1.65
            elif move == '高强度运动（沉重的体力劳动&运动员）':
                calories *= 1.80
            elif move == '重度运动（每天至少8小时剧烈运动）':
                calories *= 2.0

            calories += calories_deficit
            if calories < 1000:
                QMessageBox.warning(self, '提示', '每日热量过少(<1000kcal/天)，请调整增减脂周期长度或目标体重')
                return
            protein = ((calories / 10.0) * 3) / 4
            fat = ((calories / 10.0) * 2) / 9
            carbs = ((calories / 10.0) * 5) / 4
            self.Metabolism_CaloriesIn_Output.setText(f'{round(calories)}kcal')
            self.Metabolism_Protein_Output.setText(f'{round(protein)}g')
            self.Metabolism_Carb_Output.setText(f'{round(carbs)}g')
            self.Metabolism_Fat_Output.setText(f'{round(fat)}g')

        except Exception:
            QMessageBox.critical(self, "Error", f"发生错误: 时间不能为0")
            return

    def allDay_calories(self):
        allDay = [0, 0, 0, 0]  # 总热量，碳，蛋，脂
        try:
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
            QMessageBox.warning(self, '提示', '无食物记录')
            return

        nutrients_data = data.get(current_date, {})
        if nutrients_data:
            for food, nutrients in data[current_date].items():
                allDay[0] += float(nutrients['calories'])
                allDay[1] += float(nutrients['carbs'])
                allDay[2] += float(nutrients['protein'])
                allDay[3] += float(nutrients['fat'])
            self.today_label_calories.setText(f"{allDay[0]} kcal")
            self.todayIn_label_carb.setText(f"{allDay[1]} g")
            self.todayIn_label_protein.setText(f"{allDay[2]} g")
            self.todayIn_label_fat.setText(f"{allDay[3]} g")
        else:
            self.today_label_calories.setText("0kcal")
            self.todayIn_label_carb.setText("0 g")
            self.todayIn_label_protein.setText("0 g")
            self.todayIn_label_fat.setText("0 g")
            return

    def todayIn_delete(self):
        item = self.listWidget.currentItem()
        if item:
            item_text = item.text()
            colon_index = item_text.find(':')
            food_to_delete = item_text[:colon_index].strip()
            print(food_to_delete)
            try:
                with open('data.json', 'r') as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
                QMessageBox.warning(self, '提示', '无食物记录')
                return

            if current_date in data and food_to_delete in data[current_date]:
                del data[current_date][food_to_delete]

                if not data[current_date]:
                    del data[current_date]

                with open('data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)

                self.updateListWidget_todayIn()
                print(f"已删除 {food_to_delete}")
                self.allDay_calories()  # 更新全天
                QMessageBox.about(self, '成功', f"已删除 {food_to_delete}")

            else:
                QMessageBox.warning(self, '提示', '未找到要删除的食物记录')
        else:
            QMessageBox.warning(self, "Error", "请先选择一个食物项。")

    def addButton_clicked(self):
        print('add button clicked')
        if not self.clicked_text:
            QMessageBox.warning(self, "Error", "请先选择一个食物项。")
            return

        try:
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if current_date not in data:
            data[current_date] = {}

        data[current_date][self.clicked_text] = {
            'calories': self.calories,
            'carbs': self.carbs,
            'protein': self.protein,
            'fat': self.fat
        }

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        self.updateListWidget_todayIn()
        print('已保存')
        self.allDay_calories()  # 更新全天
        QMessageBox.about(self, '成功', '已添加')

    def listWidgetItemClicked(self, item):
        global search_result

        self.clicked_text = item.text().strip()
        clicked_nutrients = None
        for food in search_result:
            if food[0] == self.clicked_text:
                clicked_nutrients = food[1]
                break

        if clicked_nutrients:
            foodCalory = clicked_nutrients['calories']
            foodFat = clicked_nutrients['fat']
            foodCarbs = clicked_nutrients['carbs']
            foodProtein = clicked_nutrients['protein']

            size = self.FoodSearch_FoodWeightOut_Label.value()

            self.calories = round((int(foodCalory.replace('kcal', '').strip()) / 100) * size, 2)
            self.carbs = round((float(foodCarbs.replace('g', '').strip()) / 100) * size, 2)
            self.protein = round((float(foodProtein.replace('g', '').strip()) / 100) * size, 2)
            self.fat = round((float(foodFat.replace('g', '').strip()) / 100) * size, 2)

            self.FoodSearch_CaloriesOut_Label.setText(f"{self.calories:.2f}")
            self.FoodSearch_CarbOut_Label.setText(f"{self.carbs:.2f}")
            self.FoodSearch_ProteinOut_Label.setText(f"{self.protein:.2f}")
            self.FoodSearch_FatOut_Label.setText(f"{self.fat:.2f}")
        else:
            QMessageBox.warning(self, "Error", "无法找到点击的食品的营养信息")

    def searchButton_Clicked(self):
        query = self.FoodSearch_FoodEnter_LineEdit.text()
        locale = 'zh_CN'
        consumer_key = '256010f6597b46ff979efee82f0289f5'
        consumer_secret = 'd06a0a60e6874617896a893073bd0fc0'
        api_url = 'https://platform.fatsecret.com/rest/server.api'
        print(query)
        params = {
            'method': 'foods.search',
            'format': 'json',
            'search_expression': query,
            'language': locale,
        }
        auth = OAuth1(
            client_key=consumer_key,
            client_secret=consumer_secret,
            signature_method='HMAC-SHA1',
            signature_type='query'
        )
        response = requests.get(api_url, params=params, auth=auth)
        try:
            response.raise_for_status()
            food_info = response.json()
            print(food_info)
            self.jsonAnalysis(food_info)
        except requests.exceptions.RequestException as e:
            print(f"HTTP请求错误: {e}")
            QMessageBox.critical(self, "Error", f"HTTP请求错误: {e}")

    def jsonAnalysis(self, data):
        global search_result
        if 'foods' in data and 'food' in data['foods']:
            foods = data['foods']['food']
            results = []
            for elements in foods:
                foodName = elements['food_name']
                foodDescr = elements['food_description']
                pattern = r'Per (.+?) - Calories: (\d+\.?\d*)kcal \| Fat: (\d+\.?\d*)g \| Carbs: (\d+\.?\d*)g \| Protein: (\d+\.?\d*)g'
                match = re.search(pattern, foodDescr)
                if match:
                    food_des_sep = {
                        'serving_size': match.group(1),
                        'calories': match.group(2) + 'kcal',
                        'fat': match.group(3) + 'g',
                        'carbs': match.group(4) + 'g',
                        'protein': match.group(5) + 'g'
                    }
                    results.append([foodName, food_des_sep])
                else:
                    print(f"未匹配到描述信息: {foodDescr}")
            search_result = self.data_filtration(results)
            self.updateListWidget(search_result)
        else:
            QMessageBox.warning(self, "No Results", "未找到与输入匹配的食物。")

    def data_filtration(self, results):
        final = [food for food in results if food[1]['serving_size'] == '100g']
        if final:
            return final
        else:
            QMessageBox.warning(self, "No Results", "未找到与输入匹配的食物。")
            return []

    def updateListWidget(self, results):
        self.FoodSearch_FoodOuput_ListWidget.clear()
        for result in results:
            food_name = result[0]
            self.FoodSearch_FoodOuput_ListWidget.addItem(food_name)

    def updateListWidget_todayIn(self):
        self.listWidget.clear()
        try:
            with open('data.json', 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if current_date in data:
            for food, nutrients in data[current_date].items():
                food_info = f"{food}: {nutrients['calories']}kcal"
                self.listWidget.addItem(food_info)


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        mainWin = MainWindow()
        mainWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"应用程序错误: {e}")
        sys.exit(1)