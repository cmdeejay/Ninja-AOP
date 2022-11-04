import customtkinter
from tasklist import TaskListFrame
from ninja_buttons import TermsAndConditions, FAQ, CopyRight, StartSelectedButton, StartAll, StopSelectedButton, StopAll


class Canvas(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#181c24",
                         width=900,
                         height=550,
                         corner_radius=0,
                         **kwargs)

        self._taskbar = TaskListFrame(master=self)
        self._terms_and_conditions = TermsAndConditions(master=self)
        self._faq = FAQ(master=self)
        self._year = CopyRight(master=self)
        self._start_selected = StartSelectedButton(master=self)
        self._stop_selected = StopSelectedButton(master=self)
        self._start_all = StartAll(master=self)
        self._stop_all = StopAll(master=self)

        self._taskbar.place(x=20, y=40)
        self._faq.place(x=140, y=530)
        self._year.place(x=675, y=530)
        self._terms_and_conditions.place(x=8, y=530)
        self._start_selected.place(x=30, y=475)
        self._stop_selected.place(x=230, y=475)
        self._start_all.place(x=450, y=475)
        self._stop_all.place(x=650, y=475)
