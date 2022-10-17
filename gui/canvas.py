import customtkinter
from tasklist import TaskList


class Canvas(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#181c24",
                         width=1000,
                         height=600,
                         corner_radius=0,
                         **kwargs)

        self.taskbar = TaskList(master=self)
        self.taskbar.place(x=20, y=40)

        self._terms_and_conditions = customtkinter.CTkButton(master=self,
                                                             text="Terms & Conditions",
                                                             text_color="white",
                                                             text_font=("Open SANS", -10),
                                                             hover_color="#181c24",
                                                             fg_color="#181c24")
        self._terms_and_conditions.place(x=15, y=530)

        self._FAQ = customtkinter.CTkButton(master=self,
                                            text="FAQ",
                                            width=20,
                                            text_color="white",
                                            text_font=("Open SANS", -10),
                                            hover_color="#181c24",
                                            fg_color="#181c24")
        self._FAQ.place(x=140, y=530)

        self._year = customtkinter.CTkButton(master=self,
                                             text="Copyright @Min Chen 2022",
                                             width=20,
                                             text_color="white",
                                             text_font=("Open SANS", -10),
                                             hover_color="#181c24",
                                             fg_color="#181c24")
        self._year.place(x=675, y=530)
