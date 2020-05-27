from tkinter import *
from tkinter import messagebox
from time import sleep

tk = Tk()
tk.title('解二連方程')
tk.geometry("400x400")
width = 4
txt_x = StringVar()
txt_y = StringVar()
txt_x.set("x={}".format(0))
txt_y.set("y={}".format(0))

def mat(son, mom):
    n = 1
    ans=[]
    while True:
        if son % n == int() and mom % n == int():
            ans.append(n)
        n += 1
        if n > son or n > mom:
            break
    return int(max(ans))

def test(m, s):
    try:
        if m == "" or m == 0:
            son=int(s)
            mom=int(10**len(s)-1)
            return str(int(son / mat(int(son), int(mom)))) + '/' + str(int(mom/mat(int(son), int(mom))))
        else:
            son=int(m + s) - int(m)
            mom=10**len(str(son))-10**len(m)
            b = mat(int(son), int(mom))
            return "{}/{}".format(int(son/b), str(int(mom/b)))
    except:
        pass
    return False
def help_do(num):
    if num == 1:
        h1 = Tk()
        h1.title("如何使用")
        h1.geometry("300x300")
        Label(h1, text="如何使用本程式?", font=("微軟正黑體", 15), fg="white", bg="gray").pack()
        Label(h1, text="1. 在方框中輸入想要的數字。\n(如果是 Y-X=N, 請變成 -X+Y=N)", fg="green", font=("微軟正黑體", 11)).pack(pady=7)
        Label(h1, text="2. 格式必須是:\na1x+b1y=c1\na2x+b2y=c2", font=("微軟正黑體", 11)).pack(pady=7)
        Label(h1, text="3. 輸入完後請按\"運算按鈕\"", font=("微軟正黑體", 11)).pack(pady=7)
        Label(h1, text="如果還有問題，請傳G-mail給我").place(x=150, y=280, anchor=CENTER)
        h1.mainloop()
    else:
        def fra_ck(o1, o2):
            if test(o1, o2):
                answer.config(text=f"Fraction: {test(o1, o2)}")
            else:
                messagebox.showerror("錯誤", "請輸入正確的格式")
                sleep(1)
                messagebox.showinfo("egg", "下期內容: 遊戲助手")
        fraction = Tk()
        fraction.title("fraction")
        fraction.geometry("400x500")
        Label(fraction, text="轉換分數", fg="white", bg="gray", font=("微軟正黑體", 15)).pack()
        Label(fraction, text="範例:", font=("微軟正黑體", 12)).pack()
        Label(fraction, text="如果是 0.25，輸入").pack()
        Label(fraction, text="No:  25").pack()
        Label(fraction, text="    Repeat:  0").pack()
        Label(fraction, text="如果是 0.16565..，不重複1，重複65，輸入").pack()
        Label(fraction, text="No:  1 , Repeat:  65").pack()
        Label(fraction, text="如果是 0.6565.，只重複65，輸入").pack()
        Label(fraction, text="No: (不要輸入), Repeat:  65").pack()
        Label(fraction, text="No: ", font=("微軟正黑體", 12)).pack()
        no = Entry(fraction, width=8)
        no.pack()

        Label(fraction, text="Repeat: ", font=("微軟正黑體", 12)).pack()
        re = Entry(fraction, width=8)
        re.pack()
        Button(fraction, text="Check", command=lambda:fra_ck(no.get(), re.get()), bd=0, bg="#e6b3ff", fg="white").pack(pady=8)
        answer = Label(fraction, text="Fraction: ",fg="#0066cc", font=("Segoe Print", 15))
        answer.pack(pady=35)
        fraction.mainloop()
        

def number_type(num):
	if int(num) == num:
		return True
	return False

def do_math(a1, a2, b1, b2, c1, c2):
    # =========== 高斯 行列式解法 ===========
    x = (c1*b2-b1*c2)/(a1*b2-a2*b1)
    y = (a1*c2-c1*a2)/(a1*b2-b1*a2)
    # =========== 高斯 行列式解法 ===========
    txt_x.set("x={}".format(int(x) if number_type(x) else x))
    txt_y.set("y={}".format(int(y) if number_type(y) else y))

def clear():
    global a1, a2, b1, b2, ans_1, ans_2
    for i in a1, a2, b1, b2, ans_1, ans_2:
        i.delete(0, END)
    txt_x.set("x=")
    txt_y.set("y=")
    
menu = Menu(tk)
tk.config(menu=menu)

help = Menu(menu)
menu.add_cascade(label="操作說明", menu=help)
help.add_command(label="如何使用", command=lambda:help_do(1))

second = Menu(menu)
menu.add_cascade(label="分數", menu=second)
second.add_command(label="轉換分數", command=lambda:help_do(2))

Label(tk, text="解二元一次連方程式", font=("微軟正黑體", 14)).grid(row=0, column=3, columnspan=5)

Label(tk, text="x").grid(row=1, column=1)
Label(tk, text="+").grid(row=1, column=2)
Label(tk, text="y").grid(row=1, column=4)
Label(tk, text="=").grid(row=1, column=5)
ans_1 = Entry(tk, width=5)
ans_1.grid(row=1, column=6)
Label(tk, text="x").grid(row=2, column=1)
Label(tk, text="+").grid(row=2, column=2)
Label(tk, text="y").grid(row=2, column=4)
Label(tk, text="=").grid(row=2, column=5)
ans_2 = Entry(tk, width=5)
ans_2.grid(row=2, column=6)

a1 = Entry(tk, width=width)
b1 = Entry(tk, width=width)
a2 = Entry(tk, width=width)
b2 = Entry(tk, width=width)

a1.grid(row=1, column=0)
a2.grid(row=2, column=0)
b1.grid(row=1, column=3)
b2.grid(row=2, column=3)
do_btn = Button(tk, text="運算", command=lambda:do_math(eval(a1.get()), eval(a2.get()) ,eval(b1.get()), eval(b2.get()), eval(ans_1.get()), eval(ans_2.get())), bd=0, bg="white", fg="black", font=("微軟正黑體", 14))
clr_btn = Button(tk, text="清除", command=clear, bd=0, bg="white", fg="black", font=("微軟正黑體", 14))
do_btn.grid(row=3, column=3, pady=10)
clr_btn.grid(row=3, column=4, columnspan=2, pady=10)
x_lab = Label(tk, textvariable=txt_x, font=("微軟正黑體", 17))
y_lab = Label(tk, textvariable=txt_y, font=("微軟正黑體", 17))
x_lab.place(x=80, y=200)
y_lab.place(x=80, y=270)

tk.mainloop()