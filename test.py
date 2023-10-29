import random
from main import Message


encrypt_dict = {1: 'Ǎ', 2: 'ǎ', 3: 'Ǐ', 4: 'ǐ', 5: 'Ǒ', 6: 'ǒ', 7: 'Ǔ', 8: 'ǔ', 9: 'Ǖ', 10: 'ǖ', 11: 'Ǘ', 12: 'ǘ',
                13: 'Ǚ', 14: 'ǚ', 15: 'Ǜ', 16: 'ǜ', 17: 'ǝ', 18: 'Ǟ', 19: 'ǟ', 20: 'Ǡ', 21: 'ǡ', 22: 'Ǣ', 23: 'ǣ',
                24: 'Ǥ', 25: 'ǥ', 26: 'Ǧ', 27: 'ǧ', 28: 'Ǩ', 29: 'ǩ', 30: 'Ǫ', 31: 'ǫ', 32: 'Ǭ'}


class Panda:
    # 加密算法逻辑：使用random库生成一个0-20的整数，将这个整数作为seed
    # seed*2 - 1
    def __init__(self, t):
        self.text = t

    def banboo(self, pas_len):  # 密码种子
        password = ""
        temp_last = ""
        if pas_len < 3:
            info = Message("密码过短")
            info.show_warning()
            return
        for i in range(1, pas_len + 1):
            password += str(random.randint(1, 9))
        # print("初始密码", password)
        original_password = password
        password_list = list(password)
        lent = len(password_list)
        # print("密码加密过后的长度", lent)
        if lent % 2 != 0 and lent >= 3:
            temp_last = password_list[len(password_list) - 1]
        password_list.pop()
        # print("密码去除最后一位的长度", len(password_list))
        for char in range(0, len(password_list) - 1, 2):
            if password_list[char + 1]:
                temp = password[char]
                password_list[char] = password_list[char + 1]
                password_list[char + 1] = temp
        password_str = ''.join(map(str, password_list))
        password_str += temp_last
        return original_password, password_str  # 加密过后的密码

    def banboo_eater(self, original_password):  # 解密密码
        password_o = list(original_password)
        temp_last = ""
        # print("密码解密的时候的原始数组", password_o)
        lent = len(password_o)
        if lent < 3:
            ab = Message("密码过短")
            ab.show_error()
            return
        if lent % 2 != 0 and lent >= 3:
            temp_last = password_o[lent - 1]
            password_o.pop()
        for char in range(0, len(password_o) - 1, 2):
            temp = password_o[char]
            password_o[char] = password_o[char + 1]
            password_o[char + 1] = temp
        # print(password_o)
        password_str = ''.join(map(str, password_o))
        password = password_str + temp_last
        return password

    def encrypt_easy(self):  # 简单加密算法
        result = ""
        if self.text:
            for char in self.text:
                print((ord(char) + 10) * 2)
                result += (chr((ord(char) + 10) * 2))
            return result
        else:
            ab = Message("错误的输入")
            ab.show_error()

    def decrypt_easy(self):  # 简单加密算法的解密
        result = ""
        if self.text:
            for char in self.text:
                char = ord(char)
                char = int(char / 2 - 10)
                result += chr(char)
            return result
        else:
            ab = Message("错误的输入")
            ab.show_error()

    def generate_count_string(self, input_str):  # 将第一轮加密的二进制数字更改为加密后的数字
        result = ""
        count = 1
        for i in range(1, len(input_str)):
            if input_str[i] == input_str[i - 1]:
                count += 1
            else:
                result += str(count) + input_str[i - 1]
                count = 1

        result += str(count) + input_str[-1]
        return result

    def decode_count_string(self, count_str):  # 将第一轮加密的数字重新分为二进制数据
        result = ""
        i = 0
        while i < len(count_str):
            count = int(count_str[i])
            digit = count_str[i + 1]

            result += digit * count
            i += 2

        return result

    def black_panda(self, pas_len):
        text = self.text
        original_text = text
        ascii_list = []  # 储存第一轮加密的结果
        two_list = []  # 用于储存第一轮加密过后的，被分为两两一组，元组的数字的数组
        second_enc = []  # 储存第二次加密的结果
        generate_count = Panda(None)
        seed, seed_en = generate_count.banboo(pas_len)
        for char in text:
            ascii_list.append(bin(ord(char))[2:])  # 将文字的ASCII码值转换为二进制数据并且添加到ascii_list 这个列表当中
        print("第一轮加密之前的", ascii_list)
        counting = 0
        for element in ascii_list:
            ascii_list[counting] = generate_count.generate_count_string(element)  # 第一轮加密
            counting += 1
        print("第一轮加密过后的", ascii_list)
        for string_data in ascii_list:
            result_tuple = ()  # 初始化空元组
            for i in range(0, len(string_data), 2):  # 将字符串两两一组添加到元组内
                result_tuple += (string_data[i:i + 2],)
            two_list.append(result_tuple)  # 将元组添加到列表中
        for tuples in two_list:
            result_tuple = ()
            for asc in tuples:
                result_tuple = (chr(int(asc)))
            second_enc.append(result_tuple)

        print("第1.5次加密", second_enc)
        # for k in two_list:
        #     for j in k:
        #         try:
        #             integer_data = int(j)
        #             print(integer_data)
        #         except ValueError:
        #             errror = Message("error occured")
        #             errror.show_error()
        # print("密码和加密过的密码分别是", seed, seed_en)

    def white_panda(self):
        pass


a = Panda("你好吗我的朋友?你 今天过的怎么样？ ")
# original, result = a.banboo()
# print(f"加密之前的密码是：{original},加密过后的密码是：{result}, 解密过后的密码是：{a.banboo_eater(result)}")
a.black_panda(7)
print(a.generate_count_string("11100011"))

# import pyautogui
# import time
#
#
# def replace_text_with_hotkey():
#     # 定义热键，这里使用Ctrl+Alt+R，你可以根据需要修改
#     hotkey = ['ctrl', 'alt', 'r']
#
#     print("等待热键触发...")
#
#     while True:
#         # 检查是否按下了热键
#         if all(pyautogui.keyDown(key) for key in hotkey):
#             # 释放按键
#             pyautogui.keyUp(hotkey)
#
#             # 获取当前剪贴板内容
#             original_text = pyautogui.hotkey('ctrl', 'c')
#
#             # 在这里添加你想要替换的逻辑，这里只是一个简单的例子
#             replaced_text = original_text.replace("replace_me", "replacement")
#
#             # 将替换后的文本粘贴回输入框
#             pyautogui.hotkey('ctrl', 'v')
#
#             print(f"已将 '{original_text}' 替换为 '{replaced_text}'")
#
#         time.sleep(0.1)  # 避免占用过多CPU资源
#
#
# if __name__ == "__main__":
#     replace_text_with_hotkey()


# import tkinter as tk
# from tkinter import font
# root = tk.Tk()
# # 获取系统上可用的字体族列
# available_fonts = font.families()
#
# # 打印可用的字体族列
# print("Available Fonts:")
# for font_family in available_fonts:
#     print(font_family)
# root.mainloop()
