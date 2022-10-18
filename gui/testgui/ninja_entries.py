import customtkinter


class TradingAccountEntry(customtkinter.CTkEntry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         placeholder_text="Trading account",
                         text_font=("Hack NF", -12),
                         bg="#202023",
                         fg="#4ec9b0",
                         corner_radius=10,
                         **kwargs)

