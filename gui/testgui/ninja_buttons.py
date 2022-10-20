import customtkinter
from PIL import Image, ImageTk


class Logo(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        logo_image = Image.open("images/logo.png").resize((50, 50))
        logo_image_tk = ImageTk.PhotoImage(logo_image)
        super().__init__(*args,
                         text="",
                         width=50,
                         height=50,
                         image=logo_image_tk,
                         hover_color="#282c3c",
                         **kwargs)


class DashboardButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        dashboard_image = Image.open("images/Dashboard.png").resize((22, 22))
        dashboard_image_tk = ImageTk.PhotoImage(dashboard_image)
        super().__init__(*args,
                         text="Dashboard",
                         text_color="#dfe8ee",
                         image=dashboard_image_tk,
                         text_font=("Open SANS", -14, "bold"),
                         hover=False,
                         **kwargs)


class NewTaskButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        new_task_image = Image.open("images/Add.png").resize((22, 22))
        new_task_image_tk = ImageTk.PhotoImage(new_task_image)
        super().__init__(*args,
                         text="New Task",
                         text_color="#dfe8ee",
                         image=new_task_image_tk,
                         text_font=("Open SANS", -14, "bold"),
                         hover=False,
                         **kwargs)


class HistoryButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        history_image = Image.open("images/History.png").resize((21, 21))
        history_image_tk = ImageTk.PhotoImage(history_image)
        super().__init__(*args,
                         text="History",
                         text_color="#dfe8ee",
                         image=history_image_tk,
                         text_font=("Open SANS", -14, "bold"),
                         hover=False,
                         **kwargs)


class TermsAndConditions(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="Terms & Conditions",
                         text_color="#dfe8ee",
                         text_font=("Open SANS", -10),
                         hover_color="#181c24",
                         fg_color="#181c24",
                         **kwargs)


class FAQ(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="FAQ",
                         width=20,
                         text_color="#dfe8ee",
                         text_font=("Open SANS", -10),
                         hover_color="#181c24",
                         fg_color="#181c24",
                         **kwargs)


class CopyRight(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="Copyright @Min Chen 2022",
                         width=20,
                         text_color="#dfe8ee",
                         text_font=("Open SANS", -10),
                         hover_color="#181c24",
                         fg_color="#181c24",
                         **kwargs)


class StartSelectedButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="start selected",
                         text_color="white",
                         height=10,
                         width=10,
                         corner_radius=17,
                         fg_color="#ff847c",  # pink
                         text_font=("Open SANS", -16, "bold"),
                         **kwargs)


class StopSelectedButton(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="stop selected",
                         text_color="white",
                         height=10,
                         width=10,
                         corner_radius=17,
                         fg_color="#48cccc",  # blue
                         text_font=("Open SANS", -16, "bold"),
                         **kwargs)


class StartAll(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="start all",
                         text_color="white",
                         height=10,
                         width=10,
                         corner_radius=40,
                         fg_color="#a553fb",  # purple
                         text_font=("Open SANS", -16, "bold"),
                         **kwargs)


class StopAll(customtkinter.CTkButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text="stop all",
                         text_color="white",
                         height=10,
                         width=10,
                         corner_radius=40,
                         fg_color="#f4a434",  # purple
                         text_font=("Open SANS", -16, "bold"),
                         **kwargs)

# class RunButton(customtkinter.CTkButton):
#     def __init__(self, *args, **kwargs):
#         run_image = Image.open("images/run.png").resize((21, 21))
#         run_image_tk = ImageTk.PhotoImage(run_image)
#         super().__init__(*args,
#                          bg='#202023',
#                          fg='#dfe8ee',
#                          image=run_image_tk,
#                          border=0,
#                          activebackground='#202023',
#                          activeforeground='#dfe8ee',
#                          **kwargs)
