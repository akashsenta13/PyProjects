'''
 A program to stores book information
 Title, Author
 year, ISBN

 User can : 
 view all records
 Search an entry
 add entry
 update entry
 delete
 close
'''

from tkinter import *
import backend


def view_cmd():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_cmd():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(),
                              year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_cmd():
    backend.insert(title_text.get(), author_text.get(), year_text.get(),
                   isbn_text.get())
    view_cmd()


def get_selected_row(event):
    global selected
    index = list1.curselection()[0]
    selected = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected[1])
    e2.delete(0, END)
    e2.insert(END, selected[2])
    e3.delete(0, END)
    e3.insert(END, selected[3])
    e4.delete(0, END)
    e4.insert(END, selected[4])


def delete_cmd():
    backend.delete(selected[0])
    view_cmd()


def update_cmd():
    backend.update(selected[0], title_text.get(), author_text.get(),
                   year_text.get(), isbn_text.get())
    view_cmd()


window = Tk()

window.wm_title('BookStore')

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=8, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# set scroll bar to list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# buttons
b1 = Button(window, text='View All', width=12, command=view_cmd)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_cmd)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Entry', width=12, command=add_cmd)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update', width=12, command=update_cmd)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete', width=12, command=delete_cmd)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
