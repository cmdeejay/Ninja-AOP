import customtkinter
from tkinter import ttk


class TaskList(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#282c3c",
                         width=770,
                         height=470,
                         corner_radius=20,
                         **kwargs)

        self._style = ttk.Style()
        self._style.theme_use("default")
        self._style.configure("Treeview",
                              background="#202434",
                              foreground="#FFFFFF",
                              fieldbackground="#282c3c",
                              rowheight=45,
                              font=("Hack NF", 9, "bold"))
        self._style.map('Treeview',
                        foreground=[('!selected', "#FFFFFF")],
                        background=[('selected', "#181c24")])
        '''
        Header Label design.
        '''
        self._label_treeview = ttk.Treeview(master=self,
                                            columns=("First Name", "Last Name", "Email Address", "Status", "Actions"),
                                            height=43,
                                            show="tree",
                                            )
        self._label_treeview.place(x=0, y=0)
        attributes = ["ID", "First Name", "Last Name", "Email Address", "Status", "Actions"]

        self._label_treeview.column(f"#0", minwidth=34, width=34, anchor="center")
        self._label_treeview.column(f"#1", minwidth=136, width=136, anchor="center")
        self._label_treeview.column(f"#2", minwidth=136, width=136, anchor="center")
        self._label_treeview.column(f"#3", minwidth=136, width=136, anchor="center")
        self._label_treeview.column(f"#4", minwidth=136, width=136, anchor="center")
        self._label_treeview.column(f"#5", minwidth=191, width=191, anchor="center")

        self._label_treeview.insert('', 'end', text='ID', values=('First Name', 'Last Name', 'Email', 'Status', 'Actions'))

        '''
        Task Bar design.
        '''
        self._treeview = ttk.Treeview(master=self,
                                      columns=("First Name", "Last Name", "Email Address", "Status", "Actions"),
                                      height=30,
                                      show="tree",
                                      )
        self._treeview.place(x=0, y=45)

        self._treeview.column(f"#0", minwidth=34, width=34, anchor="center")
        self._treeview.column(f"#1", minwidth=136, width=136, anchor="center")
        self._treeview.column(f"#2", minwidth=136, width=136, anchor="center")
        self._treeview.column(f"#3", minwidth=136, width=136, anchor="center")
        self._treeview.column(f"#4", minwidth=136, width=136, anchor="center")
        self._treeview.column(f"#5", minwidth=191, width=191, anchor="center")

        self._treeview.tag_configure("odd", background="#282c3c", foreground="#FFFFFF")
        self._treeview.tag_configure("even", background="#202434", foreground="#FFFFFF")

        self._treeview.insert('', 'end', text='01', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='02', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='03', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='04', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='05', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='06', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        self._treeview.insert('', 'end', text='07', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        self._treeview.insert('', 'end', text='08', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
