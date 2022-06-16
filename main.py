import tkinter
import tkinter as tk

root=tk.Tk()
root.title('READ')

def read():
    f=open("C\Users\C605\Desktop\Marvel.txt")
    x=print(f.readline())
    T=tkinter.Text(root,width=200, height=400)
    T.insert(tk.END,chars=x)



button=tkinter.Button(root, text='Read', width=20, command=read())
button.pack()
root.mainloop()