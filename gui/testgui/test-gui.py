import customtkinter
import threading
from user import Username
# from utilities.ninja_utilities import Utilities
# from utilities.functions import add_task, show_client_id
# from utilities.salesforce_monitor import monitor_final
from PIL import Image, ImageTk
from ninja_buttons import DashboardButton, NewTaskButton, HistoryButton, Logo
from ninja_entries import TradingAccountEntry
from ninja_labels import UserLabel
from ninja_frames import Canvas


class GUI(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        # login_session = Utilities().login()
        super().__init__(*args, **kwargs)
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("theme/default_theme.json")
        # variable = StringVar(root)
        # variable.set("Type")
        # self.resizable(False, False)
        self['background'] = '#282c3c'
        self.iconbitmap(r'images/Ninja.ico')
        self.title("NINJA 2.2.0")
        self._window_width = 1050
        self._window_height = 555
        self._screen_width = self.winfo_screenwidth()
        self._screen_height = self.winfo_screenheight()
        self._center_x = int(self._screen_width / 2 - self._window_width / 2)
        self._center_y = int(self._screen_height / 2 - self._window_height / 2)
        self.geometry(f'{self._window_width}x{self._window_height}+{self._center_x}+{self._center_y}')

        self._left_frame = Canvas(master=self)
        self._left_frame.grid(column=1, padx=0, pady=0, sticky="E", rowspan=15)

        # self._logo = Logo(master=self)
        # self._logo.grid(row=0, column=0, padx=85, pady=0, sticky="WN")

        self._dashboard_button = DashboardButton(master=self)
        self._dashboard_button.grid(row=1, column=0, padx=30, pady=3, sticky="WW")

        self._history_button = HistoryButton(master=self)
        self._history_button.grid(row=2, column=0, padx=19, pady=3, sticky="WW")

        self._new_task_button = NewTaskButton(master=self)
        self._new_task_button.grid(row=3, column=0, padx=26, pady=3, sticky="WW")

        self._trading_login_entry = TradingAccountEntry(master=self)
        self._trading_login_entry.grid(row=4, column=0, padx=40, pady=3, sticky="W")

        self._dashboard_name = UserLabel(master=self)
        self._dashboard_name.grid(row=12, column=0, padx=30, pady=3, sticky="WS")

        # Button configure
        # Button(root, bg='#202023', fg='#b5cea8', text="SHOW", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=show_client_id, args=(trading_login_entry, client_id_entry, email_entry)).start()).place(x=355, y=55, height=30, width=80)
        # Button(root, bg='#202023', fg='#b5cea8', text="ADD TASK", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: add_task(variable, trans_btn, del_btn, run_btn, id_btn, eye_btn, email_entry, client_id_entry, first_name_entry, last_name_entry, root, login_session)).place(x=270, y=95, height=30, width=80)
        # Button(root, bg='#202023', fg='#b5cea8', text="MONITOR", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=monitor_final).start()).place(x=355, y=95, height=30, width=80)
        # Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='China', value='China', font=('Arial', 10, 'bold'), variable=variable).place(x=260, y=140)
        # Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='Other', value='Other', font=('Arial', 10, 'bold'), variable=variable).place(x=330, y=140)


gui = GUI()
gui.mainloop()
