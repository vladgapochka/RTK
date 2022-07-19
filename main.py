
import csv
import tkinter
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import tkinter as tk

type_1=[]
type_2=[]
type_3=[]
with open('tipe.csv', newline="") as f:
    reader = csv.reader(f, delimiter=';')
    count = 0
    for row in reader:
        if count == 0:
            count += 1
        else:
            type_1.append(row[0])
            type_2.append(row[1])
            type_3.append(row[2])

type_1_ = list(set(type_1))
type_2_ = list(set(type_2))
type_3_ = list(set(type_3))
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id_rule'])
    e2.insert(0,select['rule_name'])
    e3.insert(0,select['queue'])
    e4.insert(0,select['rank'])
# def Add_tr():
#     id_rule = e1.get()
#     rule_name = e2.get()
#     queue = e3.get()
#     rank = e4.get()
#
#     mysqldb = mysql.connector.connect(host="localhost", user="mysql", password="mysql", database="routing_rules")
#     mycursor = mysqldb.cursor()
#
#     try:
#         sql = "INSERT INTO `rule`(`id_rule`, `rule_name`, `queue`, `rank`) VALUES (%s,%s,%s,%s)"
#         val = (id_rule, rule_name, queue, rank)
#         mycursor.execute(sql, val)
#         mysqldb.commit()
#         lastid = mycursor.lastrowid
#
#         e1.delete(0, END)
#         e2.delete(0, END)
#         e3.delete(0, END)
#         e4.delete(0, END)
#         e1.focus_set()
#         new_rule()
#         root.destroy()
#
#     except Exception as e:
#         print(e)
#         mysqldb.rollback()
#         mysqldb.close()
def Add():
    id_rule = e1.get()
    rule_name = e2.get()
    queue = e3.get()
    rank = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="mysql", password="mysql", database="routing_rules")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO `routing_rule`(`id_rule`, `rule_name`, `queue`, `rank`) VALUES (%s,%s,%s,%s)"
        val = (id_rule, rule_name, queue, rank)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
        new_rule()
        root.destroy()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def new_rule():
    global attribute_0
    new_w=Tk()
    new_w.geometry("800x500")
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print(select)
    root.destroy()
    # btn=ttk.Button(new_w, text="Add",command = Add_tr, width= 6).place(x=10, y=230)
    type_label = ttk.Label(new_w, text="Тип")
    type_label.grid(column=0, row=0, padx=5, pady=5)
    attr_label = ttk.Label(new_w, text="Атрибут")
    attr_label.grid(column=1, row=0, padx=5, pady=5)
    oper_label = ttk.Label(new_w, text="Оператор")
    oper_label.grid(column=2, row=0, padx=5, pady=5)
    value_label = ttk.Label(new_w, text="Значение")
    value_label.grid(column=3, row=0, padx=5, pady=5)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="routing_rules")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT `type`, `attribute`, `operator`, `value` FROM `rule` WHERE `id_rule`=1")
    records = mycursor.fetchall()
    type_0 = ttk.Entry(new_w)
    type_1 = ttk.Entry(new_w)
    type_2 = ttk.Entry(new_w)
    type_3 = ttk.Entry(new_w)
    type_4 = ttk.Entry(new_w)
    type_5 = ttk.Entry(new_w)
    type_6 = ttk.Entry(new_w)
    attribute_0 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_0.grid(column=1, row=1)
    attribute_1 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_1.grid(column=1, row=2)
    attribute_2 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_2.grid(column=1, row=3)
    attribute_3 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_3.grid(column=1, row=4)
    attribute_4 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_4.grid(column=1, row=5)
    attribute_5 = ttk.Combobox(new_w, values=[
        "Тип задания 1", "Тип задания 2", "Тип задания 3", "Способ связи", "Признак запроса ОГВ", "Признак соответствия суммы критериям НС"
    ])
    attribute_5.grid(column=1, row=6)
#---------------------------------------------------
    operator_0 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_0.grid(column=2, row=1)
    operator_1 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_1.grid(column=2, row=2)
    operator_2 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_2.grid(column=2, row=3)
    operator_3 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_3.grid(column=2, row=4)
    operator_4 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_4.grid(column=2, row=5)
    operator_5 = ttk.Combobox(new_w, values=[
        "==", "!="
    ])
    operator_5.grid(column=2, row=6)
#--------------------------------------------
    value_0 = ttk.Combobox(new_w, values=type_1_)
    value_0.grid(column=3, row=1)
    value_1 = ttk.Combobox(new_w, values=type_2_)
    value_1.grid(column=3, row=2)
    value_2 = ttk.Combobox(new_w, values=type_3_)
    value_2.grid(column=3, row=3)
    value_3 = ttk.Combobox(new_w, values=["СМС", "Звонок", "Email","Письмо", "Информирование не требуется"])
    value_3.grid(column=3, row=4)
    value_4 = ttk.Combobox(new_w, values=[
        "Да", "Нет"
    ])
    value_4.grid(column=3, row=5)
    value_5 = ttk.Combobox(new_w, values=[
        "Да", "Нет"
    ])
    value_5.grid(column=3, row=6)
#-----------------------------------------------------

    for i, (id, stname, course, fee) in enumerate(records, start=0):
        if(i==0):
            type_0.insert(0, str(id))
            type_0.grid(column=0, row=i+1, padx=5, pady=5)
        if(i==1):
            type_1.insert(0, str(id))
            type_1.grid(column=0, row=i + 1, padx=5, pady=5)
        if (i == 2):
            type_2.insert(0, str(id))
            type_2.grid(column=0, row=i + 1, padx=5, pady=5)
        if (i == 3):
            type_3.insert(0, str(id))
            type_3.grid(column=0, row=i + 1, padx=5, pady=5)
        if (i == 4):
            type_4.insert(0, str(id))
            type_4.grid(column=0, row=i + 1, padx=5, pady=5)
        if (i == 5):
            type_5.insert(0, str(id))
            type_5.grid(column=0, row=i + 1, padx=5, pady=5)
        if (i == 6):
            type_6.insert(0, str(id))
            type_6.grid(column=0, row=i + 1, padx=5, pady=5)

    new_w.mainloop()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="mysql", password="mysql", database="routing_rules")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT * FROM `routing_rule`")
    records = mycursor.fetchall()
    print(records)


    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()



root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="Название").place(x=10, y=40)
Label(root, text="Очередь").place(x=10, y=70)
Label(root, text="Ранг").place(x=10, y=100)
e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)
cols = ('id_rule', 'rule_name', 'queue', 'rank')
listBox = ttk.Treeview(root, columns=cols, show='headings')
Button(root, text="Add",command = Add, width= 6).place(x=10, y=130)
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=0, y=172)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
