""" 대화상자 """

''' 불러오기'''
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *

''' 함수 '''
# def func_open():
#     messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")
# def func_exit():
#     window.quit()
#     window.destroy()
def func_open() :
    filename = askopenfilename(parent = window, initialdir="C:/python/bigdata_programing/gif", filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*"))) ## 경로?
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
def func_exit():
    window.quit()
    window.destroy()

''' 윈도우 객체 '''
window = Tk()
window.geometry("400x100")
window.title("그림!")

### 수 입력 ###
label1 = Label(window, text = "입력된 값")
label1.pack()
# label2 = Label(window, text = "선택 파일 이름")
# label2.pack()

value = askinteger("확대배수", "주사위 숫자(1~6) 입력", minvalue = 1, maxvalue = 6)
label1.configure(text = str(value))

### 파일 읽기 ###
# filename = askopenfilename(parent = window, filetypes = (("GIF 파일","*.gif"),("모든 파일","*.*")))
# label2.configure(text = str(filename))
### 파일 저장 ###
# saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg",
#             filetypes = (("JPG 파일", "*.jpg;*.jpeg"), ("모든 파일","*.*")))
# label2.configure(text = saveFp)
# saveFp.close()

### 사진 읽기 ###
photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand = 1, anchor = CENTER)


''' 메뉴 객체 '''
mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "열기",command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "종료",command = func_exit)

window.mainloop()