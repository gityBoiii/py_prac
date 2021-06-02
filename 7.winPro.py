"""윈도우 프로그래밍"""

from tkinter import *
from tkinter import messagebox

window = Tk() ## window ins

'''함수'''
def bark() :
    messagebox.showinfo("멍멍!", "와후우우우우~")
def chk_bt():
    if chk.get() == 0 :
        messagebox.showinfo("", "꺼짐!")
    else :
        messagebox.showinfo("", "켜짐!")
def lang_select() :
    if  var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")


'''글 설정'''
label1 = Label(window, text = "이것은 제목이다")
label2 = Label(window, text = "부제목이다", font = ("궁서체", 30), fg = "blue")
label3 = Label(window, text = "글이다", bg = "magenta", width = 20, height = 5, anchor = SE, fg = "red")
'''사진 설정'''
photo1 = PhotoImage(file = "doggo_sleep.gif", width = 100, height = 100)
label4 = Label(window, image = photo1)
photo2 = PhotoImage(file = "shiba.gif", width = 100, height = 100)
'''버튼 설정'''
button1 = Button(window, text = "끝!", fg = "red", command = quit)
button2 = Button(window, image = photo2, command = bark)
chk = IntVar() ## cb1 init
cb1 = Checkbutton(window, text = "클릭", variable = chk, command = chk_bt)
var = IntVar() ## rb1 init
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = lang_select)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = lang_select)
rb3 = Radiobutton(window, text= "Java", variable = var, value = 3, command = lang_select)
btnListR = [None] * 3
for i in range(0, 3):
    btnListR[i] = Button(window, text = "버튼R" + str(i + 1))
btnListT = [None] * 3
for i in range(0, 3):
    btnListT[i] = Button(window, text = "버튼T" + str(i + 1))
btnListB = [None] * 3
for i in range(0, 3):
    btnListB[i] = Button(window, text = "버튼B" + str(i + 1))

'''글 생성'''
label1.pack()
label2.pack()
label3.pack()
''' 사진 생성'''
label4.pack()
'''버튼 생성'''
button1.pack()
button2.pack()
cb1.pack()
rb1.pack(side=LEFT)
rb2.pack(side=LEFT)
rb3.pack(side=LEFT)
for btn in btnListR :
    btn.pack(side = RIGHT, fill=X, padx=10, pady=10) ##padding
for btn in btnListT :
    btn.pack(side=TOP, fill=X, ipadx=10, ipady=10) ##inside padding
for btn in btnListB :
    btn.pack(side = BOTTOM, fill = X, ipadx = 10, ipady = 10,
    padx = 10, pady = 10) ##both padding

window.title("타이틀") ##title
window.geometry("1200x800")
window.resizable(width = False, height= True) ## resize = false
window.mainloop() ## exicute


