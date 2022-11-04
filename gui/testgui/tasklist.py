import customtkinter
from tkinter import ttk
from ninja_treeviews import TaskList, TaskListHeader
from ninja_scrollbar import TreeViewScrollbar


class TaskListFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#282c3c",
                         width=790,
                         height=450,
                         **kwargs)

        self._label_treeview = TaskListHeader(master=self)
        self._label_treeview.grid(row=0)

        self._treeview = TaskList(master=self)
        self._treeview_scrollbar = TreeViewScrollbar(master=self._treeview)
        self._treeview.configure(yscrollcommand=self._treeview_scrollbar.set)
        #self._treeview.place(x=0, y=45)
        self._treeview.grid(row=1, sticky='N', pady=1)

       # self._treeview_scrollbar.grid(column=1)

        self._treeview.insert('', 'end', text='01', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved',), tags='odd')
        self._treeview.insert('', 'end', text='02', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='03', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='04', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='05', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='06', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='07', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='08', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='09', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='10', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='11', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='12', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='13', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='13', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
