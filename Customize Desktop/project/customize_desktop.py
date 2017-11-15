#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import threading

class PointOfSale:
    def __init__(self, master):

        # Master root window customization
        master.title('MobileIT POS')
        master.iconbitmap('images/pos_back_white_icon.ico')
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        self.master = master
        self.tab_notebook = ttk.Notebook(master, width=1200, height=600)
        self.tab_notebook.pack()

        # Style font
        self.s = ttk.Style()
        self.s.configure('Blue.TLabelframe.Label', font=('courier', 15, 'bold'))
        self.s.configure('Blue.TLabelframe.Label', foreground='blue')
        self.s.configure('Green.TLabelframe.Label', font=('courier', 20, 'bold'))
        self.s.configure('Green.TLabelframe.Label', foreground='green')
     #   self.s.configure('Red.TLabelframe.Label', background='blue')

        # Define images
        self.green_circle_image = PhotoImage(file='images/green_circle.png').subsample(2, 2)
        self.red_circle_image = PhotoImage(file='images/red_circle.png').subsample(1, 1)
        self.pos_image = PhotoImage(file='images/POS.png').subsample(5, 5)
        self.management_image = PhotoImage(file='images/management_logo.png').subsample(5, 5)
        self.support_image = PhotoImage(file='images/support.png').subsample(5, 5)
        self.restart_tablet_image = PhotoImage(file='images/restart_tablet.png').subsample(5, 5)
        self.start_application_image = PhotoImage(file='images/start_application.png').subsample(5, 5)
        self.stop_application_image = PhotoImage(file='images/stop_application.png').subsample(5, 5)
        self.stop_tablet_image = PhotoImage(file='images/stop_tablet.png').subsample(14, 14)

        self.devices_status_red_lcd_image = PhotoImage(file='images/red_square_lcd.png').subsample(5, 5)
        self.devices_status_green_lcd_image = PhotoImage(file='images/green_square_lcd.png').subsample(5, 5)
        self.devices_status_red_gsm_image = PhotoImage(file='images/red_square_gsm.png').subsample(5, 5)
        self.devices_status_green_gsm_image = PhotoImage(file='images/green_square_gsm.png').subsample(5, 5)
        self.devices_status_red_barcode_image = PhotoImage(file='images/red_square_barcode.png').subsample(5, 5)
        self.devices_status_green_barcode_image = PhotoImage(file='images/green_square_barcode.png').subsample(5, 5)
        self.devices_status_red_pyweb_image = PhotoImage(file='images/red_square_pyweb.png').subsample(5, 5)
        self.devices_status_green_pyweb_image = PhotoImage(file='images/green_square_pyweb.png').subsample(5, 5)

        self.devices_status_recheck_image = PhotoImage(file='images/recheck.png').subsample(5, 5)
        self.settings_image = PhotoImage(file='images/management_logo.png').subsample(5, 5)

        self.support_admin_access_image = PhotoImage(file='images/admin_access.png').subsample(5, 5)
        self.support_remote_access_image = PhotoImage(file='images/remote_access.png').subsample(2, 2)
        self.support_contact_image = PhotoImage(file='images/support.png').subsample(2, 2)
        #Backup image
        self.support_red_backup_image = PhotoImage(file='images/red_square_backup.png').subsample(5, 5)
        self.support_green_backup_image = PhotoImage(file='images/green_square_backup.png').subsample(5, 5)


        # App Tab
        self.app_tab_frame = ttk.Frame(self.tab_notebook, width=1200, height=600)
        self.app_tab_frame.pack()

        # Header App Frame
        self.header_app_tab_frame = ttk.LabelFrame(self.app_tab_frame, text="Welcome to your Point Of Sale application",  style = "Blue.TLabelframe" )
        self.header_app_tab_frame.config(relief = RIDGE)
        self.header_app_tab_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)
        ttk.Label(self.header_app_tab_frame, image=self.pos_image).pack(side = LEFT , expand = True, fill = BOTH)
        ttk.Label(self.header_app_tab_frame, text='EASILY Manage your business !',  font=("Helvetica", 15, "bold")).pack(side = LEFT , expand = True, fill = BOTH)
        # Hour clock
        self.timeText = ttk.Label(self.header_app_tab_frame, text="Time", font=("Helvetica", 15), relief="sunken", anchor="center")
        self.timeText.pack(side = LEFT , expand = True, fill = BOTH)


        # App Power Frame
        self.app_power_frame = ttk.LabelFrame(self.app_tab_frame, text="Application Power Management",  style = "Blue.TLabelframe" )
        self.app_power_frame.config(relief = RIDGE)
        self.app_power_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)
        self.start_app_button = ttk.Button(self.app_power_frame, image=self.start_application_image, command=self.start_nativefier)
        self.start_app_button.pack(side = LEFT , expand = True, fill = BOTH)
        self.stop_app_button = ttk.Button(self.app_power_frame, image=self.stop_application_image, command=self.stop_nativefier)
        self.stop_app_button.pack(side = LEFT , expand = True, fill = BOTH)
        self.status_app_image = ttk.Label(self.app_power_frame, image=self.red_circle_image)
        self.status_app_image.pack(side = LEFT , expand = True, fill = BOTH, padx=150, pady=10)

        # Tablet Power Frame
        self.tablet_power_frame = ttk.LabelFrame(self.app_tab_frame, text="Tablet Power Management",  style = "Blue.TLabelframe")
        self.tablet_power_frame.config(relief = RIDGE)
        self.tablet_power_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)
        self.restart_tablet_button = ttk.Button(self.tablet_power_frame, image=self.restart_tablet_image, command=self.restart_tablet)
        self.restart_tablet_button.pack(side = LEFT , expand = True, fill = BOTH, padx=150, pady=10)
        self.stop_tablet_button = ttk.Button(self.tablet_power_frame, image=self.stop_tablet_image, command=self.stop_tablet)
        self.stop_tablet_button.pack(side = LEFT , expand = True, fill = BOTH, padx=150, pady=10)

        # Add tab to root Window
        self.tab_notebook.add(self.app_tab_frame, text = 'Application')

        # Management Tab
        self.management_tab_frame = ttk.Frame(self.tab_notebook, width=1200, height=600)
        self.management_tab_frame.pack()

        # Header Management Frame
        self.header_management_tab_frame = ttk.LabelFrame(self.management_tab_frame, text="Monitoring and Administtration",  style = "Blue.TLabelframe" )
        self.header_management_tab_frame.config(relief = RIDGE)
        self.header_management_tab_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)
        ttk.Label(self.header_management_tab_frame, image=self.settings_image).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.header_management_tab_frame, text='Manage your tablet !').grid(row=1, column=1)

        # Devices status Frame
        self.devices_status_frame = ttk.LabelFrame(self.management_tab_frame, text="Devices Status",  style = "Blue.TLabelframe" )
        self.devices_status_frame.config(relief = RIDGE)
        self.devices_status_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)

        self.devices_status_lcd_image = ttk.Label( self.devices_status_frame, image=self.devices_status_red_lcd_image)
        self.devices_status_lcd_image.pack(side = LEFT , expand = True, fill = BOTH)
        self.devices_status_barcode_image = ttk.Label(self.devices_status_frame, image=self.devices_status_red_barcode_image )
        self.devices_status_barcode_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_gsm_image = ttk.Label(self.devices_status_frame, image=self.devices_status_red_gsm_image)
        self.devices_status_gsm_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_pyweb_image = ttk.Label(self.devices_status_frame, image=self.devices_status_red_pyweb_image)
        self.devices_status_pyweb_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_recheck_button = ttk.Button(self.devices_status_frame, image=self.devices_status_recheck_image, command=self.status_recheck)
        self.devices_status_recheck_button.pack(side = LEFT , expand = True, fill = BOTH)

        # Management Support Frame
        self.support_frame = ttk.LabelFrame(self.management_tab_frame, text="Support",  style = "Blue.TLabelframe")
        self.support_frame.config(relief = RIDGE)
        self.support_frame.pack(side = TOP , expand = True, fill = BOTH, padx=10, pady=10)

        self.support_admin_access_button = ttk.Button(self.support_frame, image=self.support_admin_access_image, command= lambda: self.admin_access(master))
        self.support_admin_access_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_remote_access_button = ttk.Button(self.support_frame, image=self.support_remote_access_image, command=self.remote_access)
        self.support_remote_access_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_contact_button = ttk.Button(self.support_frame, image=self.support_contact_image, command=self.support_contact)
        self.support_contact_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_backup_button = ttk.Button(self.support_frame, image=self.support_red_backup_image, command=self.support_contact)
        self.support_backup_button.pack(side=LEFT, expand=True, fill=BOTH)


        # Add tab to root Window
        self.tab_notebook.add(self.management_tab_frame, text='Management and Settings')






    def restart_tablet(self):
        print(messagebox.askyesno(title='restart tablet', message='Do you want to restart the tablet ?',  icon="warning"))
        print("restart_tablet")

    def stop_tablet(self):
        print(messagebox.askyesno(title='stop tablet', message='Do you want to shutdown the tablet ?',  icon="warning"))
        print("stop_tablet")

    def start_nativefier(self):
        #self.status_app_image = ttk.Label(self.app_power_frame, image=self.green_circle_image)
        #self.status_app_image.pack(side = LEFT , expand = True, fill = BOTH, padx=150, pady=10)
        self.status_app_image.configure(image=self.green_circle_image)
        print("start_nativefier")

    def stop_nativefier(self):
        print(messagebox.askyesno(title='stop Application', message='Do you want to stop application ?',  icon="warning"))
        self.status_app_image.configure(image=self.red_circle_image)
        print("stop_nativefier")

    def status_recheck(self):
        print("status_recheck")

    def admin_access(self, master):

        username = ("Tom")
        password = ("")

        def try_login(window, master):
            print("Trying to login...")
            if username_guess.get() == username:
                messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In. \n "
                                                      "The Customize Desktop will be close !", icon="info")
                window.destroy()
                master.destroy()
            else:
                messagebox.showinfo("-- ERROR --", "Please enter valid infomation! \n"
                                                   "Please try again with right account", icon="warning")
                window.destroy()

        # Gui Things
        window = Toplevel(master)
        window.resizable(width=FALSE, height=FALSE)
        window.title("Log-In")
        window.geometry("200x150")
        window.attributes("-topmost", True)

        # Creating the username & password entry boxes
        username_text = ttk.Label(window, text="Username:")
        username_guess = ttk.Entry(window)
        password_text = ttk.Label(window, text="Password:")
        password_guess = ttk.Entry(window, show="*")

        # attempt to login button
        attempt_login = ttk.Button(window, text="Login", command= lambda: try_login(window, master))


        username_text.pack()
        username_guess.pack()
        password_text.pack()
        password_guess.pack()
        attempt_login.pack()
        # Main Starter
        window.mainloop()

        print("admin_access")

    def remote_access(self):
        print(messagebox.askyesno(title='Remote access', message='Do you want to enable remote access ? \n'
                                                                'Make sure the support are ready to proceed ! ',  icon="info"))
        print("remote_access")

    def support_contact(self):
        message = ['Tel : +237 000000000', 'Facebook : facebook/mobileITPOS', 'whatsapp : +237 000000000', 'Email : mobileitafrica@gmail.com']
        messagebox.showinfo(title='MobileIT POS', message="\n".join(message),  icon="info")
        print("support_contact")

    def update_timeText(self):
        # Get the current time, note you can change the format as you wish
        current = time.strftime("%Y-%m-%d %H:%M:%S")
        # Update the timeText Label box with the current time
        self.timeText.configure(text=current)
        # Call the update_timeText() function after 1 second
        self.master.after(1000, self.update_timeText)

    # Cron job
    def printit(self):
        threading.Timer(3600.0, self.printit).start()
        print("Hello, World!")

def main():

    root = Tk()

    root.geometry('{}x{}'.format( 1024, 600))
    pointofsale = PointOfSale(root)
    pointofsale.update_timeText()
    pointofsale.printit()
    root.mainloop()


if __name__ == "__main__": main()
