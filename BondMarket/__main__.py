from unittest.main import MAIN_EXAMPLES
import customtkinter as ctk
import gui.menue_frame as menue_frame
import gui.status_bar as status_bar
from app.app_state import AppState, create_all_dir, process_exists
from tkinter import messagebox
import threading



def check_if_ms_is_running(app_state: AppState) -> None:
    if process_exists('Mail Service.exe'):
        messagebox.showinfo('BondMarket', 'BondMarket cannot be used when\nthe mail service is running.!')
        main_root.quit()
    else:
        pass


def exit(app_state: AppState) -> None:
    app_state.save_settings()
    if app_state.save_state is False:
        app_state.save_array() if messagebox.askokcancel('BondMarket', 'exit_message') else None
    main_root.quit()


def mainloop() -> None:
    """_summary_
    """
    
    t = threading.Thread(target=(lambda: check_if_ms_is_running(app_state)))

    global main_root
    create_all_dir()
    app_state = AppState()
    # Set up main Window
    app_state.load_settings()
    ctk.set_appearance_mode(app_state.settings["app_settings"]["appearance"])
    app_state.load_array()
    for i in range(10):
        app_state.append_expenditure(f"Person {i+1}", i+1.0, 'Test Test Test', '2022.06.01')
    ctk.set_default_color_theme(r'Themes\theme.json')
    main_root = ctk.CTk()
    # Custom up main Window
    main_root.geometry(
        f"{main_root.winfo_screenwidth()}x{main_root.winfo_screenheight()}")
    main_root.state('zoomed')
    main_root.title('')
    main_root.iconbitmap(r'Icons\BondMarket_Icon.ico')
    main_root.protocol('WM_DELETE_WINDOW', lambda: exit(app_state))
    status_bar.draw_status_bar(main_root)
    menue_frame.draw_menue(main_root, app_state)
    t.start()
    main_root.mainloop()


if __name__ == '__main__':
    mainloop()
