# -*- coding: UTF-8 -*-

# подключаем библеотеки
from tkinter import *
from tkinter import filedialog

logo = "PyText++"

# открыть файл
def open_file():
    global fn
    fn = filedialog.Open(root, filetypes=[('Все файлы', '.*')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())
    root.title(fn + " - PyText++ (UNREDISTERED)")

# создать файл
def new_file():
    fn = filedialog.SaveAs(root, filetypes=[('Все файлы', '.*')]).show()
    if fn == '':
        return
    if not fn.endswith(""):
        fn += ".*"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

# сохранить файл
def save_file():
    fr = 3

# об приложении
def About():
    win = Toplevel(root)
    win.title(logo)
    win.geometry("300x130")
    label1 = Label(win, text="PyTxt", font="Arial 24", bg="#2d2d30", fg="#ffffff", height=1)
    label2 = Label(win, text="Unregistered", font="Arial 9", bg="#2d2d30", fg="#ffffff")
    label3 = Label(win, text="Copyright 2019 PyTxt", font="Arial 10", bg="#2d2d30", fg="#ffffff", height=4)
    label1.pack(fill=X)
    label2.pack(fill=X)
    label3.pack(side=BOTTOM, fill=X)

# выход из приложения
def Exit():
    global root
    root.destroy()


# создаём цикл tkinter
root = Tk()
root.title(logo + " (UNREDISTERED)")
root.geometry("1280x555")

main_menu = Menu(root)
root.configure(menu=main_menu, bg="#1e1e1e")

# меню приложения (file)
item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=item)
item.add_command(label="  New File                                              Ctrl+N", command=new_file)
item.add_command(label="  Open File...                                         Ctrl+0", command=open_file)
item.add_command(label="  Save  ", command=save_file)
item.add_separator()
#item.add_command(label="  Close File                                            Ctrl+W", command=close_file)
item.add_command(label="  Exit  ", command=Exit)

# edit
item2 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Edit", menu=item2)
item2.add_command(label="  Copy                                                  Ctrl+C")
item2.add_command(label="  Cut                                                     Ctrl+X")
item2.add_command(label="  Paste                                                  Ctrl+V")

# help
item3 = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="help", menu=item3)
item3.add_command(label="  About Pytxt  ", command=About)

# редактор
global textFrame
textFrame = Frame(root, height=640, width=600)
textFrame.pack(fill=X, side=TOP)


textbox = Text(textFrame, font='Roboto 15 italic', wrap='word', bg="#2d2d30", fg="#ffffff")
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

# статус бар
status_bar = Label(root, relief=SUNKEN, anchor=W, text=" debug complete...", bg="#007acc", fg="#ffffff", width=300)
status_bar.pack(side=BOTTOM, fill=Y)

root.mainloop()
