import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


class Message:
    def __init__(self, info):
        self.info = info

    def show_info(self):
        messagebox.showinfo("Information", f"{self.info}")

    def show_warning(self):
        messagebox.showwarning("Warning", f"{self.info}")

    def show_error(self):
        messagebox.showerror("Error", f"{self.info}")


class Panda:
    # 加密算法逻辑：使用random库生成一个0-20的整数，将这个整数作为seed
    # seed*2 - 1
    def __init__(self, t, pas_len):
        self.text = t
        self.pas_len = pas_len

    def banboo(self):  # 密码种子
        password = ""
        password_list = []
        temp_last = ""
        if self.pas_len < 3:
            info = Message("密码过短")
            info.show_warning()
            return
        for i in range(1, self.pas_len):
            password += str(random.randint(1, 9))
            password = str(int(password) * 2 - 1)
            password_list = list(password)
        lent = len(password_list)
        if lent % 2 != 0 and lent >= 3:
            temp_last = password_list[len(password_list) - 1]
            password_list.pop()
        for char in range(0, len(password_list) - 1, 2):
            if password_list[char + 1]:
                temp = password[char]
                password_list[char] = password_list[char + 1]
                password_list[char + 1] = temp
        password_str = ''.join(map(str, password_list))
        password_str += temp_last
        return password_str

    def banboo_eater(self):  # 解密密码
        use = Panda(self.text, self.pas_len)
        password_o = list(use.banboo())
        temp_last = ""
        print(password_o)
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
        print(password_o)
        password_str = ''.join(map(str, password_o))
        password = int(password_str)
        password = str((int(password) + 1) / 2)
        password = password + temp_last
        return password

    def encrypt_easy(self):  # 简单加密算法
        result = ""
        if self.text:
            for char in self.text:
                print((ord(char) + 10) * 2)
                result += (chr((ord(char) + 10) * 2))
            return result
        else:
            a = Message("错误的输入")
            a.show_error()

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


def entry_get_jia():
    t = l_4.get()
    panda = Panda(t, None)
    result = panda.encrypt_easy()
    pyperclip.copy(result)
    ab = Message(f"加密后的内容已经复制到剪贴板：{result}")
    ab.show_info()


def entry_get_jie():
    t = l_4.get()
    panda = Panda(t, None)
    result = panda.decrypt_easy()
    pyperclip.copy(result)
    ab = Message(f"解密后的内容已经复制到剪贴板：{result}")
    ab.show_info()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("加密小程序")
    root.geometry("1000x800")
    bold_font = ("Unispace", 15, "bold")
    l_3 = tk.Label(root, text="请输入的要加密或者解密的文字", font=bold_font)
    l_4 = tk.Entry(root)
    l_5 = tk.Label(root, text="请选择加密/解密", font=bold_font)

    button_1 = tk.Button(root, text="加密", font=bold_font, command=entry_get_jia)
    button_2 = tk.Button(root, text="解密", font=bold_font, command=entry_get_jie)
    l_3.place(x=350, y=200, width=300, height=50)
    l_4.place(x=350, y=250, width=300, height=50)
    button_1.place(x=350, y=450, width=140, height=50)
    button_2.place(x=500, y=450, width=140, height=50)
    root.mainloop()
