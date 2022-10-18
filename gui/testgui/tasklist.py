import customtkinter
from tkinter import ttk
from ninja_treeviews import TaskList, TaskListHeader


class TaskListFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#282c3c",
                         width=790,
                         height=470,
                         **kwargs)

        self._label_treeview = TaskListHeader(master=self)
        self._label_treeview.place(x=0, y=0)

        self._treeview = TaskList(master=self)
        self._treeview.place(x=0, y=45)

