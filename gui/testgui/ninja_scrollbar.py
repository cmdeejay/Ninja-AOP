import customtkinter


class TreeViewScrollbar(customtkinter.CTkScrollbar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         orientation='vertical',
                         bg_color='#181c24',
                         width=8,
                         corner_radius=20,
                         **kwargs)

