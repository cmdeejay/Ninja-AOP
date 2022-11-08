import customtkinter
from ninja_buttons import TermsAndConditions, FAQ, CopyRight, StartSelectedButton, StartAll, StopSelectedButton, StopAll
from ninja_treeviews import TaskList, TaskListHeader
from ninja_scrollbar import TreeViewScrollbar


class Canvas(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#181c24",
                         width=900,
                         height=650,
                         corner_radius=0,
                         **kwargs)

        self._taskbar = TaskListFrame(master=self)
        self._button_container = ButtonContainer(master=self)
        self._link_container = LinksContainer(master=self)

        self._taskbar.grid(padx=20, pady=(20, 0))
        self._button_container.grid(padx=0, sticky="S")
        self._link_container.grid(padx=(15, 0))


class TaskListFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#282c3c",
                         width=850,
                         height=400,
                         **kwargs)

        self._label_treeview = TaskListHeader(master=self)
        self._label_treeview.grid(padx=0, pady=0)

        self._treeview = TaskList(master=self)
        self._treeview.grid(padx=0, pady=0)

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
        # self._treeview.insert('', 'end', text='12', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='even')
        # self._treeview.insert('', 'end', text='13', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')
        # self._treeview.insert('', 'end', text='13', values=('Charmy', 'Chen', 'Charmy.chen@gmail.com', 'ID is approved'), tags='odd')


class ButtonContainer(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#181c24",
                         width=790,
                         height=45,
                         **kwargs)

        self._start_selected = StartSelectedButton(master=self)
        self._stop_selected = StopSelectedButton(master=self)
        self._start_all = StartAll(master=self)
        self._stop_all = StopAll(master=self)

        self._start_selected.pack(in_=self, side="left", padx=25, pady=20)
        self._stop_selected.pack(in_=self, side="left", padx=25, pady=20)
        self._start_all.pack(in_=self, side="left", padx=25, pady=20)
        self._stop_all.pack(in_=self, side="left", padx=25, pady=20)


class LinksContainer(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#181c24",
                         width=790,
                         height=45,
                         **kwargs)

        self._terms_and_conditions = TermsAndConditions(master=self)
        self._faq = FAQ(master=self)
        self._year = CopyRight(master=self)

        self._terms_and_conditions.grid(column=0, row=0, padx=0, pady=30, sticky="W")
        self._faq.grid(column=1, row=0, padx=5, pady=30)
        self._year.grid(column=2, row=0, padx=(465, 0), pady=30)
