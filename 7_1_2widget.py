""" 키 이벤트 """

from tkinter import *
from tkinter import messagebox

''' 함수 '''
def clickLeft(event):
    messagebox.showinfo("제목임", "클릭!")
def clickImage(event):
    messagebox.showinfo("ㅎㅎ", "토끼!")
def clickMouse(event) :
    txt = ""
    if  event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이("
    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨"
    label2.configure(text = txt)
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트", "너가 누른 키는 " + chr(event.keycode))



''' 윈도우 '''
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "gif/rabbit.gif")
label1 = Label(window, image = photo)
label2 = Label(window, text = "잘봐")

#window.bind("<Button-1>", clickLeft("마우스"))
label1.bind("<Button>", clickImage)
label2.bind("<Button>", clickMouse)
window.bind("<Key>", keyEvent)


label1.pack(expand = 1, anchor = CENTER)
label2.pack(expand = 1, anchor = CENTER)


window.mainloop()

