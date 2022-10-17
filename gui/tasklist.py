import customtkinter


class TaskList(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         fg_color="#282c3c",
                         width=800,
                         height=470,
                         corner_radius=20,
                         **kwargs)
