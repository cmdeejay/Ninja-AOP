import customtkinter
from tkinter import ttk
from ninja_treeviews import TaskList


class TaskListHeader(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         columns=("First Name", "Last Name", "Email Address", "Status", "Actions"),
                         height=43,
                         show="tree",
                         **kwargs)

        self._header_style = ttk.Style()
        self._header_style.theme_use("default")
        self._header_style.configure(style="Treeview",
                                     foreground="#FFFFFF",
                                     background="#202434",
                                     fieldbackground="#282c3c",
                                     rowheight=45,
                                     font=("Hack NF", 9, "bold"))
        self._header_style.map(style='Treeview',
                               foreground=[('!selected', "#FFFFFF")],
                               background=[('selected', "#202434")])

        attributes = ["ID", "First Name", "Last Name", "Email Address", "Status", "Actions"]

        self.column(f"#0", minwidth=34, width=34, anchor="center")
        self.column(f"#1", minwidth=136, width=136, anchor="center")
        self.column(f"#2", minwidth=136, width=136, anchor="center")
        self.column(f"#3", minwidth=156, width=156, anchor="center")
        self.column(f"#4", minwidth=136, width=136, anchor="center")
        self.column(f"#5", minwidth=191, width=191, anchor="center")
        self.insert('', 'end', text='ID', values=('First Name', 'Last Name', 'Email', 'Status', 'Actions'))

