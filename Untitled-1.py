from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('660x450')
win.configure(bg='#ffeee6')
num=1
#=======func===========
def exit():
    win.destroy()

def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_personnelcode.delete(0,END)
    ent_salary.delete(0,END)
    ent_fname.focus_set()

def tax():
    salary = int(ent_salary.get())
    tax = salary * 0.1
    lbl_tax.configure(text=f'{tax}')

def insert():
    global num
    fname = ent_fname.get()
    lname = ent_lname.get()
    personnelcode = ent_personnelcode.get()
    salary = ent_salary.get()
    if fname == '' or lname == '' or personnelcode == '' or salary == '':
        messagebox.showerror('eror','You have to input data!!!')
        return
    else:        
        lst.insert(END,f'{num},{fname},{lname},{personnelcode},{salary}')
        num+=1
        clear()

def show(event):
    index = lst.curselection()
    data = lst.get(index)
    list_ = data.split(',')
    clear()
    ent_fname.insert(END,list_[1])
    ent_lname.insert(END,list_[2])
    ent_personnelcode.insert(END,list_[3])
    ent_salary.insert(END,list_[4])


#=======widget===========
'''label'''
lbl_fname = Label(win,text='fname',font='cambria 16 bold',bg='#ffeee6')
lbl_fname.grid(row=0,column=0,padx=10,pady=10)

lbl_lname = Label(win,text='lname',font='cambria 16 bold',bg='#ffeee6')
lbl_lname.grid(row=0,column=3,padx=10,pady=10)

lbl_personnelcode = Label(win,text='personnel code',font='cambria 16 bold',bg='#ffeee6')
lbl_personnelcode.grid(row=1,column=0,padx=10,pady=10)

lbl_salary = Label(win,text='salary',font='cambria 16 bold',bg='#ffeee6')
lbl_salary.grid(row=1,column=3,padx=10,pady=10)

lbl_tax = Label(win,text='Tax...',font='cambria 18 bold',width=9,bg='#ffccff')
lbl_tax.place(x=500,y=113)

'''entry'''
ent_fname = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_fname.grid(row=0,column=2,padx=2,pady=10)

ent_lname = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_lname.grid(row=0,column=4,padx=2,pady=10)

ent_personnelcode = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_personnelcode.grid(row=1,column=2,padx=2,pady=10)

ent_salary = Entry(win,font='cambria 14 bold',bg='#ffccff',width=16)
ent_salary.grid(row=1,column=4,padx=2,pady=10)

'''button'''
btn_clear =Button(win,text='clear',font='cambria 14 bold',bg='#ffccff',width=11,command=clear)
btn_clear.place(x=50,y=110)

btn_exit =Button(win,text='exit',font='cambria 14 bold',bg='#ffccff',width=11,command=exit)
btn_exit.place(x=200,y=110)

btn_tax =Button(win,text='tax',font='cambria 14 bold',bg='#ffccff',width=11,command=tax)
btn_tax.place(x=350,y=110)

btn_insert =Button(win,text='insert',font='cambria 14 bold',bg='#ffccff',width=11,command=insert)
btn_insert.place(x=50,y=160)

'''listbox'''
lst = Listbox(win,font='cambria 14 bold',bg='#ffccff',width=55,height=7)
lst.place(x=25,y=210)
lst.bind('<<ListboxSelect>>',show)

win.mainloop()