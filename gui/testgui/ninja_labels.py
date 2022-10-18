import customtkinter
from user import Username


class UserLabel(customtkinter.CTkLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         text=f"{Username.user}",
                         text_color="white",
                         text_font=("Hack NF", -11),
                         **kwargs)
