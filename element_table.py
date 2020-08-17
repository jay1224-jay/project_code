from tkinter import *
from tkinter import messagebox
import random
import time
import threading

class ele_class:

	def __init__(self):
		self.elements = [
		'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
		'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 
		'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Te', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 
		'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 
		'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm','Md', 'No', 'Lr', 
		'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc' , 'Lv', 'Ts', 'Og'
		]# all element: 118
		self.ch_ele = [
		'氫', '氦', '鋰', '鈹', '硼', '碳', '氮', '氧', '氟', '氖', '鈉', '鎂', '鋁', '矽', '磷', '硫', '氯', '氬', 
		'鉀', '鈣', '鈧', '鈦', '釩', '鉻', '錳', '鐵', '鈷', '鎳', '銅', '鋅', 
		'鎵', '鍺', '砷', '硒', '溴', '氪', '銣', '鍶', '釔', '鋯', '鈮', '鉬', '鍀', '釕', '銠', '鈀', '銀', '鎘', '銦', '錫', '銻', '碲', '碘', '氙', '銫', '鋇', 
		'鑭', '鈰', '鐠', '釹', '鉕', '釤', '銪', '釓', '鋱', '鏑', '鈥', '鉺', '銩', '鐿', '鎦', 
		'鉿', '鉭', '鎢', '錸', '鋨', '銥', '鉑', '金', '汞', '鉈', '鉛', '鉍', '釙', '砹', '氡', '法', '鐳',
		'錒', '釷', '鏷', '鈾', '錼', '鈽', '鋂', '鋦', '鉳', '鉲', '鑀', '鐨', '鍆', '鍩', '鐒',
		'鑪', '𨧀', '𨭎', '𨨏', '𨭆', '䥑', '鐽', '錀', '鎶', '鉨', '鈇', '鏌', '鉝', '钿', '澳'
		]
		self.test = {}
		for i in range(len(self.elements)):
		    self.test[self.elements[i]] = self.ch_ele[i]
		for i in range(len(self.elements)):
		    self.test[self.ch_ele[i]] = self.elements[i]
		self.tk = Tk()
		self.tk.attributes('-fullscreen', True)
		self.tk.config(bg='#353D34')
		Label(self.tk, text='開發者: 王宥傑', fg='black', bg='SystemButtonFace').place(x=1200, y=680)
		Button(self.tk, text='結束全螢幕', command=lambda: self.tk.attributes('-fullscreen', False), font=('', 15)).place(x=1000, y=680)
		self.index_face()

	def is_english(self, text):
		self.alpha = [chr(x) for x in range(65, 91)]
		return True if [True for w in text if w.upper() in self.alpha] else False

	def index_face(self):
		try:
			self.search_main.pack_forget()
		except:
			pass
		try:
			self.quiz_check.pack_forget()
		except:
			pass
		try:
			self.end_result.pack_forget()
		except:
			pass
		try:
			self.test_face.pack_forget()
		except:
			pass
		self.index_main = Frame(self.tk)
		Label(self.index_main, text='元素週期表程式', font=('微軟正黑體', 20)).pack(pady=30)
		Label(self.index_main, text='歡迎來到元素程式，請選擇你要使用的功能:', font=('微軟正黑體', 15)).pack()
		Button(self.index_main, text='搜尋元素', command=self.search_face).pack(pady=40)
		Button(self.index_main, text='考我元素', command=self.quiz_face).pack()
		self.index_main.pack(pady=150)
		self.tk.mainloop()

	def search_face(self):
		self.index_main.pack_forget()
		self.search_main = Frame()
		Label(self.search_main, text="搜尋元素", font=('微軟正黑體', 20)).grid(row=0, column=0, columnspan=2, pady=20)
		Label(self.search_main, text="請輸入元素名稱:  ", font=('微軟正黑體', 13)).grid(row=1, column=0)
		self.ele_name = Entry(self.search_main)
		self.ele_name.insert(0, '中英文都可')
		self.ele_name.grid(row=1, column=1)
		Button(self.search_main, text="搜尋", command=lambda: self.search(self.ele_name.get())).grid(row=2, column=0, pady=10)
		Button(self.search_main, text='清除', command=self.del_name).grid(row=2, column=1, pady=10)

		Label(self.search_main, text='Name: ', font=('微軟正黑體', 15)).grid(row=3, column=0)
		self.obj_name = Label(self.search_main, text="", font=('微軟正黑體', 20))
		self.obj_name.grid(row=3, column=1)
		Label(self.search_main, text='中文名稱: ', font=('微軟正黑體', 15)).grid(row=5, column=0)
		Label(self.search_main, text="英文名稱: ", font=('微軟正黑體', 15)).grid(row=6, column=0)
		Label(self.search_main, text='原子序: ', font=('微軟正黑體', 15)).grid(row=7, column=0)
		Label(self.search_main).grid(row=4, column=0, columnspan=2)
		self.ch_n = Label(self.search_main, text="", font=('微軟正黑體', 15))
		self.en_n = Label(self.search_main, text="", font=('微軟正黑體', 15))
		self.ele_index = Label(self.search_main, text='', font=('微軟正黑體', 15))
		self.ch_n.grid(row=5, column=1)
		self.en_n.grid(row=6, column=1)
		self.ele_index.grid(row=7, column=1)
		Button(self.search_main, text="回到主頁面", command=self.index_face).grid(row=8, column=0, columnspan=2)
		self.search_main.pack(pady=130)

	def show_r_w(self, lists, userindex):
		if lists[userindex] == self.a_b_t[self.count][1] :
			self.test_face.pack_forget()
			self.right_face.pack(pady=150)
			time.sleep(1)
			self.right_face.pack_forget()
			self.test_face.pack(pady=150)
		else:
			self.test_face.pack_forget()
			self.wrong_face.pack(pady=150)		
			time.sleep(2)
			self.wrong_face.pack_forget()
			self.test_face.pack(pady=150)
		if self.count == len(self.a_b_t):
			self.test_face.pack_forget()
	def search(self, search_name):
		try:
			self.ch_n.config(text=self.test[search_name.title()] if self.is_english(search_name) else search_name)
			self.en_n.config(text=search_name.title() if self.is_english(search_name) else self.test[search_name.title()].title())
			self.ele_index.config(text=str(self.elements.index(search_name.title())+1 if self.is_english(search_name) else self.ch_ele.index(search_name)+1))
			self.obj_name['text'] = search_name.title()
		except:
			messagebox.showerror('', '請輸入正確的名稱!')
		self.ele_name.delete(0, END)
	def del_name(self):
		self.ele_name.delete(0, END)
	def the_end(self):
		self.quiz.config(text=len(self.a_b_t))
		self.right_quiz.config(text=str(self.right))
		self.wrong_quiz.config(text=str(self.wrong))
		self.persent.config(text=f'答對率: {round(self.right*100/len(self.a_b_t))}%')
		time.sleep(2)
		self.end_result.pack(pady=150)

	def check_right_wrong(self, ques, user_index):
		self.t = threading.Thread(target=self.show_r_w, args=(ques, user_index))
		#self.t_wrong = threading.Thread(target=self.)
		if ques[user_index] == self.a_b_t[self.count][1]:
			self.right += 1		
			self.t.start()
		else:
			self.wrong += 1
			self.no.config(text=f'答錯了!\n{self.a_b_t[self.count][0]}是 {self.a_b_t[self.count][1]}')
			self.t.start()
		self.count += 1
		
		if self.count == len(self.a_b_t): # 結束
			threading.Thread(target=self.the_end).start()
		else:
			self.question.config(text=self.a_b_t[self.count][0])
			for i in range(0, 4):
				eval('self.ans'+str(1+i)).config(text=self.all_question[self.count][i])
	def stop(self):
		self.test_face.pack_forget()
		self.index_main.pack(pady=150)
			
	def go_test(self):
		self.quiz_check.pack_forget()
		self.checked = []
		self.a_b_t = [] # after be tested   1: answer 0: question
		for i in self.var:
			if self.var[i].get() == True:
				self.p = self.save_ele[i].split()
				if self.mode.get() == 'ec' : self.p.reverse()
				self.checked.append(self.p)
		if self.checked:
			if self.which.get() == '有':
				self.a_b_t = self.checked
			else:
				if self.mode.get() == 'ec':
					for i in range(len(self.elements)):
						if [self.elements[i], self.ch_ele[i]] not in self.checked:
							self.a_b_t.append([self.elements[i], self.ch_ele[i]])
				else:
					for i in range(len(self.elements)):
						if [self.ch_ele[i], self.elements[i]] not in self.checked:
							self.a_b_t.append([self.ch_ele[i], self.elements[i]])
			random.shuffle(self.a_b_t)
			# ====== testing =======
			self.test_bg = '#353D34'
			self.test_face = Frame(self.tk, bg=self.test_bg)
			Label(self.test_face, text='請選擇答案', bg=self.test_bg, fg='white', font=('微軟正黑體', 12)).grid(row=0, column=1, columnspan=2)
			self.question = Label(self.test_face, text='question', bg=self.test_bg, fg='white', font=('微軟正黑體', 16))
			self.question.grid(row=1, column=1, columnspan=2)
			Button(self.test_face, text='結束', command=self.stop).grid(row=3, column=0)
			self.answer = IntVar()
			self.ans1 = Radiobutton(self.test_face, text='test', variable=self.answer, value=0, font=('微軟正黑體', 15))
			self.ans2 = Radiobutton(self.test_face, text='test', variable=self.answer, value=1, font=('微軟正黑體', 15))
			self.ans3 = Radiobutton(self.test_face, text='test', variable=self.answer, value=2, font=('微軟正黑體', 15))
			self.ans4 = Radiobutton(self.test_face, text='test', variable=self.answer, value=3, font=('微軟正黑體', 15))
			self.ans1.grid(row=2, column=0)
			self.ans2.grid(row=2, column=1)
			self.ans3.grid(row=2, column=2)
			self.ans4.grid(row=2, column=3)
			self.test_face.pack(pady=150)
			self.right = 0
			self.wrong = 0
			self.count = 0
			self.all_question = []
			for i in range(len(self.a_b_t)):
				self.be_show=[]
				while len(self.be_show) != 3:
					self.choose = random.choice(self.ch_ele if self.mode.get() == 'ec' else self.elements)
					if self.choose != self.a_b_t[i][1] : self.be_show.append(self.choose)
				self.be_show.append(self.a_b_t[i][1])
				random.shuffle(self.be_show)
				random.shuffle(self.be_show)
				self.all_question.append(self.be_show)

			self.question.config(text=self.a_b_t[0][0])
			self.ans1.config(text=self.all_question[0][0])
			self.ans2.config(text=self.all_question[0][1])
			self.ans3.config(text=self.all_question[0][2])
			self.ans4.config(text=self.all_question[0][3])
			Button(self.test_face, text='確定', command=lambda: self.check_right_wrong(self.all_question[self.count], self.answer.get()), font=('微軟正黑體', 12), border=0, bg='white').grid(row=3, column=1, columnspan=2, pady=30)
			self.right_face = Frame(self.tk, bg='green')
			self.wrong_face = Frame(self.tk, bg='red')
			Label(self.right_face, text='答對了!', bg='green', fg='white', font=('微軟正黑體', 17)).pack(anchor=CENTER, pady=100, padx=100)
			self.no = Label(self.wrong_face, text='答錯了!', bg='red', fg='white', font=('微軟正黑體', 17))
			self.no.pack(anchor=CENTER, pady=100, padx=100)

			self.end_result = Frame(self.tk)
			Label(self.end_result, text='恭喜你結束了這個測驗', font=('微軟正黑體', 17)).grid(row=0, column=0, columnspan=2)
			Label(self.end_result, text='你的結果如下:', font=('微軟正黑體', 17)).grid(row=1, column=0, columnspan=2)
			Label(self.end_result, text='題數: ', font=('微軟正黑體', 15)).grid(row=2, column=0)
			self.quiz = Label(self.end_result, text='', font=('微軟正黑體', 15))			
			self.quiz.grid(row=2, column=1)
			Label(self.end_result, text='答對: ', font=('微軟正黑體', 15)).grid(row=3, column=0)
			self.right_quiz = Label(self.end_result, text='', font=('微軟正黑體', 15))
			self.right_quiz.grid(row=3, column=1)
			Label(self.end_result, text='答錯: ', font=('微軟正黑體', 15)).grid(row=4, column=0)
			self.wrong_quiz = Label(self.end_result, text='', font=('微軟正黑體', 15))
			self.wrong_quiz.grid(row=4, column=1)
			self.persent = Label(self.end_result, text='答對率: ', font=('微軟正黑體', 15))
			self.persent.grid(row=5, column=0, columnspan=2)
			Button(self.end_result, text="回到主頁面", command=self.index_face).grid(row=6, column=0, columnspan=2)

		else:
			self.quiz_check.pack(pady=80)
			messagebox.showerror('', '請勾選元素，謝謝')

		# ====== testing =======
	def quiz_face(self):
		self.index_main.pack_forget()
		self.quiz_check = Frame(self.tk)
		self.which = StringVar()
		self.which.set('有')
		self.mode = StringVar()
		self.mode.set('ce')
		Label(self.quiz_check, text='請勾選元素', font=('微軟正黑體', 17)).grid(row=0, column=8, columnspan=2)
		Radiobutton(self.quiz_check, text='考我有勾的', variable=self.which, value='有', font=('微軟正黑體', 12)).grid(row=3, column=3, columnspan=2)
		Radiobutton(self.quiz_check, text='考我沒勾的', variable=self.which, value='沒', font=('微軟正黑體', 12)).grid(row=4, column=3, columnspan=2)
		Radiobutton(self.quiz_check, text='中文->元素名稱', variable=self.mode, value='ce').grid(row=3, column=7, columnspan=2)
		Radiobutton(self.quiz_check, text='元素名稱->中文', variable=self.mode, value='ec').grid(row=4, column=7, columnspan=2)
		Button(self.quiz_check, text='開始', command=self.go_test).grid(row=3, column=9, columnspan=2)
		# ====== 週期表 ======
		self.save_ele = {x: self.ch_ele[x]+' '+self.elements[x] for x in range(len(self.elements))}
		self.var = {i: BooleanVar() for i in range(len(self.elements))}
		Checkbutton(self.quiz_check, text='氫 H', variable=self.var[0], font=('微軟正黑體', 13)).grid(row=2, column=0, sticky=W)
		Checkbutton(self.quiz_check, text='氦 He', variable=self.var[1], font=('微軟正黑體', 13)).grid(row=2, column=17, sticky=W)
		Checkbutton(self.quiz_check, text='鋰 Li', variable=self.var[2], font=('微軟正黑體', 12)).grid(row=3, column=0, sticky=W)
		Checkbutton(self.quiz_check, text='鈹 Be', variable=self.var[3], font=('微軟正黑體', 12)).grid(row=3, column=1, sticky=W)
		Checkbutton(self.quiz_check, text='硼 B', variable=self.var[4], font=('微軟正黑體', 12)).grid(row=3, column=12, sticky=W)
		Checkbutton(self.quiz_check, text='碳 C', variable=self.var[5], font=('微軟正黑體', 12)).grid(row=3, column=13, sticky=W)
		Checkbutton(self.quiz_check, text='氮 N', variable=self.var[6], font=('微軟正黑體', 12)).grid(row=3, column=14, sticky=W)
		Checkbutton(self.quiz_check, text='氧 O', variable=self.var[7], font=('微軟正黑體', 12)).grid(row=3, column=15, sticky=W)
		Checkbutton(self.quiz_check, text='氟 F', variable=self.var[8], font=('微軟正黑體', 12)).grid(row=3, column=16, sticky=W)
		Checkbutton(self.quiz_check, text='氖 Ne', variable=self.var[9], font=('微軟正黑體', 12)).grid(row=3, column=17, sticky=W)
		Checkbutton(self.quiz_check, text='鈉 Na', variable=self.var[10], font=('微軟正黑體', 12)).grid(row=4, column=0, sticky=W)
		Checkbutton(self.quiz_check, text='鎂 Mg', variable=self.var[11], font=('微軟正黑體', 12)).grid(row=4, column=1, sticky=W)
		Checkbutton(self.quiz_check, text='鋁 Al', variable=self.var[12], font=('微軟正黑體', 12)).grid(row=4, column=12, sticky=W)
		Checkbutton(self.quiz_check, text='矽 Si', variable=self.var[13], font=('微軟正黑體', 12)).grid(row=4, column=13, sticky=W)
		Checkbutton(self.quiz_check, text='磷 P', variable=self.var[14], font=('微軟正黑體', 12)).grid(row=4, column=14, sticky=W)
		Checkbutton(self.quiz_check, text='硫 S', variable=self.var[15], font=('微軟正黑體', 12)).grid(row=4, column=15, sticky=W)
		Checkbutton(self.quiz_check, text='氯 Cl', variable=self.var[16], font=('微軟正黑體', 12)).grid(row=4, column=16, sticky=W)
		Checkbutton(self.quiz_check, text='氬 Ar', variable=self.var[17], font=('微軟正黑體', 12)).grid(row=4, column=17, sticky=W)
		self.a = 5
		self.b=0
		for n in range(18, 54):
			Checkbutton(self.quiz_check, text=f'{self.ch_ele[n]} {self.elements[n].title()}', variable=self.var[n], font=('微軟正黑體', 12)).grid(row=self.a, column=self.b, sticky=W)
			self.b += 1
			if n == 35:
				self.a += 1
				self.b = 0

		Checkbutton(self.quiz_check, text='銫 Cs', variable=self.var[54], font=('微軟正黑體', 12)).grid(row=7, column=0, sticky=W)
		Checkbutton(self.quiz_check, text='鋇 Ba', variable=self.var[55], font=('微軟正黑體', 12)).grid(row=7, column=1, sticky=W)
		Label(self.quiz_check, text='鑭系', font=('微軟正黑體', 12)).grid(row=7, column=2)
# font=('微軟正黑體', 20)
		for n in range(71, 86):
			Checkbutton(self.quiz_check, text=f'{self.ch_ele[n]} {self.elements[n].title()}', variable=self.var[n], font=('微軟正黑體', 12)).grid(row=7, column=n-68, sticky=W)

		Checkbutton(self.quiz_check, text='法 Fr', variable=self.var[86], font=('微軟正黑體', 12)).grid(row=8, column=0, sticky=W)
		Checkbutton(self.quiz_check, text='鐳 Ra', variable=self.var[87], font=('微軟正黑體', 12)).grid(row=8, column=1, sticky=W)
		Label(self.quiz_check, text='錒系', font=('微軟正黑體', 12)).grid(row=8, column=2)
		for n in range(103, 118):
			Checkbutton(self.quiz_check, text=f'{self.ch_ele[n]} {self.elements[n].title()}', variable=self.var[n], font=('微軟正黑體', 12)).grid(row=8, column=n-100, sticky=W)

		self.b = 3
		# ==== 藍 =====
		for n in range(56, 71):
			Checkbutton(self.quiz_check, text=f'{self.ch_ele[n]} {self.elements[n].title()}', variable=self.var[n], font=('微軟正黑體', 12)).grid(row=9, column=self.b, sticky=W)
			self.b += 1
		# ==== 阿 =====
		self.b = 3
		for n in range(88, 103):
			Checkbutton(self.quiz_check, text=f'{self.ch_ele[n]} {self.elements[n].title()}', variable=self.var[n], font=('微軟正黑體', 12)).grid(row=10, column=self.b, sticky=W)
			self.b += 1
		# ====== 週期表 ======
		Button(self.quiz_check, text="回到主頁面", command=self.index_face).grid(row=9, column=0, columnspan=2)
		self.quiz_check.pack(pady=80)

def main():
	ele_class()

if __name__ == '__main__':
	main()