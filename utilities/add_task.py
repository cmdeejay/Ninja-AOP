from tkinter import ttk
import tkinter as tk
import threading
from utilities.functions import NinjaFunctions

task_counter = 0


def addTask(variable, trans_btn, del_btn, run_btn, id_btn, eye_btn, email_entry, client_id_entry, first_name_entry, last_name_entry, root, login_session):
    global task_counter
    new_task_counter = task_counter + 1
    for cou in range(task_counter, new_task_counter):
        empty_order_label = ttk.Label(root, text=str(cou+1), style='White_small.TLabel')
        empty_order_label.place(x=25, y=250 + 25 * (cou - 1))

        email_label = ttk.Label(root, text=email_entry.get(), style='White_small.TLabel')
        email_label.place(x=65, y=250 + 25 * (cou - 1))
        email = email_label.cget('text')

        client_id_label = ttk.Label(root, text=client_id_entry.get(), style='White_small.TLabel')
        client_id_label.place(x=277, y=250 + 25 * (cou - 1))
        client_id = client_id_label.cget('text')

        first_name_label = ttk.Label(root, text=first_name_entry.get(), style='White_small.TLabel')
        first_name_label.place(x=371, y=250 + 25 * (cou - 1))
        first_name = first_name_label.cget('text')

        last_name_label = ttk.Label(root, text=last_name_entry.get(), style='White_small.TLabel')
        last_name_label.place(x=518, y=250 + 25 * (cou - 1))
        last_name = last_name_label.cget('text')

        status_label = ttk.Label(root, text='', style='White_small.TLabel')
        status_label.place(x=663, y=250 + 25 * (cou - 1))

        NinjaFunction = NinjaFunctions(email, client_id, first_name, last_name, login_session, status_label)

        action_run_button = tk.Button(root, bg='#202023', fg='white', image=run_btn, border=0, activebackground='#202023', activeforeground='white',
                                      command=lambda: threading.Thread(target="", args=(variable, email_label.cget("text"), login_session, first_name_label.cget("text"), last_name_label.cget('text'), client_id_label.cget("text"), status_label)).start())
        action_visit_button = tk.Button(root, bg='#202023', fg='white', image=eye_btn, border=0, activebackground='#202023', activeforeground='white',
                                        command=lambda: threading.Thread(target="", args=(client_id_label.cget("text"), email_label.cget("text"))).start())
        action_show_id_button = tk.Button(root, bg='#202023', fg='white', image=id_btn, border=0, activebackground='#202023', activeforeground='white',
                                          command=lambda: threading.Thread(target=NinjaFunction.idDocuments).start())
        action_trans_id_button = tk.Button(root, bg='#202023', fg='white', image=trans_btn, border=0, activebackground='#202023', activeforeground='white',
                                           command=lambda: threading.Thread(target=NinjaFunction.idTranslation).start())
        action_del_button = tk.Button(root, bg='#202023', fg='white', image=del_btn, border=0, activebackground='#202023', activeforeground='white',
                                      command=lambda: threading.Thread(target="", args=(empty_order_label, client_id_label, email_label, first_name_label, action_trans_id_button, last_name_label, action_run_button, action_show_id_button, action_visit_button, action_del_button, status_label)).start())

        action_run_button.place(x=870, y=250 + 25 * (cou - 1))
        action_visit_button.place(x=957, y=249 + 25 * (cou - 1))
        action_show_id_button.place(x=895, y=249 + 25 * (cou - 1))
        action_trans_id_button.place(x=930, y=249 + 25 * (cou - 1))
        action_del_button.place(x=990, y=249 + 25 * (cou - 1))
        task_counter = new_task_counter


