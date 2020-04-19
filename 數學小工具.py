from tkinter import *
from tkinter import messagebox
import random


class main():
    def __init__(self):
        self.main_fun()
    def main_fun(self):
        self.tk = Tk()
        self.tk.title("數學小工具")
        self.tk.geometry("400x300")
        self.title = Label(self.tk, text="請選擇檢測的項目:", font=("微軟正黑體", 16))
        self.title.pack()
        Button(self.tk, text="最小公倍數", width=10, fg="black", font=("微軟正黑體", 12), command=self.pub_small, bd=0).pack(padx=5, pady=5)
        Button(self.tk, text="最大公因數", width=10, fg="black", font=("微軟正黑體", 12), command=self.pub_big, bd=0).pack(padx=5, pady=5)
        Button(self.tk, text="質數", width=10, fg="black", font=("微軟正黑體", 12), command=self.Prime, bd=0).pack(padx=5, pady=5)
        Button(self.tk, text="合數", width=10, fg="black", font=("微軟正黑體", 12), command=self.other_num, bd=0).pack(padx=5, pady=5)
        Button(self.tk, text="Quit", bd=0, fg="white", bg="#4d4d4d", command=self.tk.destroy, font=("微軟正黑體", 12)).pack(anchor=S, side=RIGHT, padx=10, pady=10)
        self.tk.mainloop()
# =============================================================================
    def pub_small(self):
        self.tk.destroy()
        self.small = Tk()
        self.small.title("最小公倍數")
        self.small.geometry("400x400")
        Label(self.small, text="最小公倍數", font=("微軟正黑體", 14)).pack()
        Label(self.small, text="第一數:",font=("微軟正黑體", 12)).place(x=33, y=41)
        self.one = Entry(self.small)
        self.one.pack(padx=10, pady=10)
        # =============================
        self.two_tx = Label(self.small, text="第二數:",font=("微軟正黑體", 12)).place(x=33, y=83)
        self.two = Entry(self.small)
        self.two.pack(padx=10, pady=10)
        # =============================
        Button(self.small, text="Run", command=lambda:self.check("s")).place(x=120, y=120)
        Button(self.small, text="Clear", command=lambda:self.clr("s")).place(x=190, y=120)
        # =============================
        Label(self.small, text="最小公倍數是:",font=("微軟正黑體", 10)).place(x=33, y=180)
        self.anw__ = Entry(self.small, width=10)
        self.anw__.place(x=180, y=180)
        Button(self.small, text="back", bd=0,command=lambda: self.back("s"), font=("微軟正黑體", 10)).pack(anchor=S, side=RIGHT, padx=5, pady=5)
        self.small.mainloop()
# =============================================================================
    def pub_big(self):
        self.tk.destroy()
        self.big = Tk()
        self.big.title("最大公因數")
        self.big.geometry("400x400")
        Label(self.big, text="最大公因數", font=("微軟正黑體", 14)).pack()
        Label(self.big, text="第一數:",font=("微軟正黑體", 12)).place(x=33, y=41)
        self.one_bg = Entry(self.big)
        self.one_bg.pack(padx=10, pady=10)
        # =============================
        Label(self.big, text="第二數:",font=("微軟正黑體", 12)).place(x=33, y=83)
        self.two_bg = Entry(self.big)
        self.two_bg.pack(padx=10, pady=10)
        # =============================
        Button(self.big, text="Run", command=lambda:self.check("b")).place(x=120, y=120)
        Button(self.big, text="Clear", command=lambda:self.clr("b")).place(x=190, y=120)    
        # =============================
        Label(self.big, text="最大公因數:",font=("微軟正黑體", 10)).place(x=33, y=180)
        self.anw__bg = Entry(self.big, width=10)
        self.anw__bg.place(x=180, y=180)
        Button(self.big, text="back", bd=0,command=lambda: self.back("b"), font=("微軟正黑體", 10)).pack(anchor=S, side=RIGHT, padx=5, pady=5)
        self.big.mainloop()
# =============================================================================
    def Prime(self):
        self.tk.destroy()
        self.prime = Tk()
        self.prime.title("質數")
        self.prime.geometry("400x300")
        Label(self.prime, text="質數", font=("微軟正黑體", 14)).pack(pady=10)
        Label(self.prime, text="檢測數字: ", font=("微軟正黑體", 12)).place(x=70, y=60)
        self.test_p = Entry(self.prime, width=13)
        self.test_p.place(x=180, y=63)
        self.result = Label(self.prime, text="", font=("微軟正黑體", 12))
        self.result.place(x=150, y=170)
        Button(self.prime, text="Check", command=lambda:self.check("p")).place(x=90, y=100)
        Button(self.prime, text="Clear", command=lambda:self.clr("p")).place(x=190, y=100)
        Button(self.prime, text="back", bd=0,command=lambda: self.back("p"), font=("微軟正黑體", 10)).pack(anchor=S, side=RIGHT, padx=5, pady=5)
        self.prime.mainloop()
# =============================================================================
    def other_num(self):
        self.tk.destroy()
        self.otn = Tk()
        self.otn.title("合數")
        self.otn.geometry("400x300")
        Label(self.otn, text="質數", font=("微軟正黑體", 14)).pack(pady=10)
        Label(self.otn, text="檢測數字: ", font=("微軟正黑體", 12)).place(x=70, y=60)
        self.test_o = Entry(self.otn, width=13)
        self.test_o.place(x=180, y=63)
        self.result_o = Label(self.otn, text="", font=("微軟正黑體", 12))
        self.result_o.place(x=150, y=170)
        Button(self.otn, text="Check", command=lambda:self.check("o")).place(x=90, y=100)
        Button(self.otn, text="Clear", command=lambda:self.clr("o")).place(x=190, y=100)
        Button(self.otn, text="back", bd=0,command=lambda: self.back("o"), font=("微軟正黑體", 10)).pack(anchor=S, side=RIGHT, padx=5, pady=5)
        self.otn.mainloop()
# =============================================================================
    def back(self, window_arg):
        if (window_arg == "s") : self.small.destroy()
        elif window_arg == "b" : self.big.destroy()
        elif window_arg == "p" : self.prime.destroy()
        elif window_arg == "o" : self.otn.destroy()
        self.main_fun()
# =============================================================================
    def clr(self, win):
        if win == "s":
            self.one.delete(0, END)
            self.two.delete(0, END)
            self.anw__.delete(0, END)
        elif win == "b":
            self.one_bg.delete(0, END)
            self.two_bg.delete(0, END)
            self.anw__bg.delete(0, END)
        elif win == "p" : self.test_p.delete(0, END)
        else : self.test_o.delete(0, END)
# =============================================================================
    def check(self, objec):
        if objec == "s":
            try:
                self.n1_sm = int(self.one.get())
                self.n2_sm = int(self.two.get())
                self.n_sm = max([self.n1_sm, self.n2_sm])
                self.greater = self.n_sm
                while(True):
                    if(self.greater % self.n1_sm == 0 and self.greater % self.n2_sm == 0):
                        self.lcm = self.greater
                        break
                    self.greater += 1
                self.anw__.delete(0, END)
                self.anw__.insert(1, self.lcm)
            except ValueError : messagebox.showerror("error", "請輸入數字")  
        elif objec == "b":
            try:
                self.n1 = int(self.one_bg.get())
                self.n2 = int(self.two_bg.get())
                self.n = 1
                self.anw = []
                while True:
                    if self.n1 % self.n == int() and self.n2 % self.n == int():
                        self.anw.append(self.n)
                    self.n += 1
                    if self.n > self.n1 or self.n > self.n2:
                        break
                self.anw__bg.delete(0, END)
                self.anw__bg.insert(1, max(self.anw))
            except ValueError : messagebox.showerror("error", "請輸入數字")
        elif objec == "p":
            try:
                self.x = 0
                self.p = int(self.test_p.get())
                if self.p < 4:
                    if self.small_pr_num(self.p):
                        self.result.configure(text="{} 是質數".format(self.p) if self.p < 4 else "{} 不是質數".format(self.p))
                else:
                    if self.p > 100 : self.n_p = [26, 34, 51]
                    else : self.n_p = random.sample(range(1, self.p), 3)
                    for i in self.n_p:
                        if (i ** self.p % self.p == i) : self.x += 1
                    self.result.configure(text="{} 是質數".format(self.p) if (self.x == 3) else "{} 不是質數".format(self.p))
            except ValueError : messagebox.showerror("error", "請輸入數字")
        else:
            try:
                self.end = []
                self.ot_ = 1
                self.ot_n = int(self.test_o.get())
                while True:
                    if self.ot_n % self.ot_ == int() : self.end.append(self.ot_)
                    self.ot_ += 1
                    if self.ot_ > self.ot_n : break
                self.result_o.configure(text="{} 是合數".format(self.ot_n) if (len(self.end) >= 3) else "{} 不是合數".format(self.ot_n))
            except ValueError : messagebox.showerror("error", "請輸入數字")
    def small_pr_num(self, num):
        if num == 0 : return False
        else : return True
# =============================================================================
main()
