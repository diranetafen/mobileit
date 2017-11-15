#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import time
import threading

os.chdir("/home/pi/pycharm/project/")


class PointOfSale:
    def __init__(self, master):

        # Master root window customization
        master.title('MobileIT POS')
        self.pos_icon_image = PhotoImage(file='images/pos_back_white.png').subsample(5, 5)
        self.master = master
        master.tk.call('wm', 'iconphoto', master._w, self.pos_icon_image)
        master.resizable(False, False)
        master.configure(background='#e1d8b9')

        # This variable help us to not run GSM test at the bootup of the tablet
        #self.test_gsm = 0

        self.tab_notebook = ttk.Notebook(master, width=1200, heigh=600)
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
        self.devices_status_red_filesystem_image = PhotoImage(file='images/red_square_filesystem.png').subsample(5, 5)
        self.devices_status_green_filesystem_image = PhotoImage(file='images/green_square_filesystem.png').subsample(5,
                                                                                                                     5)
        self.devices_status_red_printer_image = PhotoImage(file='images/red_square_printer.png').subsample(5, 5)
        self.devices_status_green_printer_image = PhotoImage(file='images/green_square_printer.png').subsample(5,
                                                                                                                     5)
        self.devices_status_red_usb_key_image = PhotoImage(file='images/red_square_usb_key.png').subsample(5, 5)
        self.devices_status_green_usb_key_image = PhotoImage(file='images/green_square_usb_key.png').subsample(5, 5)

        self.devices_status_recheck_image = PhotoImage(file='images/recheck.png').subsample(5, 5)
        self.settings_image = PhotoImage(file='images/management_logo.png').subsample(5, 5)

        self.support_admin_access_image = PhotoImage(file='images/admin_access.png').subsample(5, 5)
        self.support_remote_access_image = PhotoImage(file='images/remote_access.png').subsample(2, 2)
        self.support_contact_image = PhotoImage(file='images/support.png').subsample(2, 2)

        # Backup image
        self.support_red_backup_image = PhotoImage(file='images/red_square_backup.png').subsample(5, 5)
        self.support_green_backup_image = PhotoImage(file='images/green_square_backup.png').subsample(5, 5)

        # App Tab
        self.app_tab_frame = ttk.Frame(self.tab_notebook, width=1200, heigh=600)
        self.app_tab_frame.pack()

        # Header App Frame
        self.header_app_tab_frame = ttk.LabelFrame(self.app_tab_frame, text="Welcome to your Point Of Sale application",
                                                   style="Blue.TLabelframe")
        self.header_app_tab_frame.config(relief=RIDGE)
        self.header_app_tab_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)
        ttk.Label(self.header_app_tab_frame, image=self.pos_image).pack(side=LEFT, expand=True, fill=BOTH)
        ttk.Label(self.header_app_tab_frame, text='EASILY Manage your business !', font=("Helvetica", 15, "bold")).pack(
            side=LEFT, expand=True, fill=BOTH)
        # Hour clock
        self.timeText = ttk.Label(self.header_app_tab_frame, text="Time", font=("Helvetica", 15), relief="sunken",
                                  anchor="center")
        self.timeText.pack(side=LEFT, expand=True, fill=BOTH)

        # App Power Frame
        self.app_power_frame = ttk.LabelFrame(self.app_tab_frame, text="Application Power Management",
                                              style="Blue.TLabelframe")
        self.app_power_frame.config(relief=RIDGE)
        self.app_power_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)
        self.start_app_button = ttk.Button(self.app_power_frame, image=self.start_application_image,
                                           command=self.start_nativefier)
        self.start_app_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.stop_app_button = ttk.Button(self.app_power_frame, image=self.stop_application_image,
                                          command=self.stop_nativefier)
        self.stop_app_button.state(['disabled'])
        self.stop_app_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.status_app_image = ttk.Label(self.app_power_frame, image=self.red_circle_image)
        self.status_app_image.pack(side=LEFT, expand=True, fill=BOTH, padx=150, pady=10)

        # Tablet Power Frame
        self.tablet_power_frame = ttk.LabelFrame(self.app_tab_frame, text="Tablet Power Management",
                                                 style="Blue.TLabelframe")
        self.tablet_power_frame.config(relief=RIDGE)
        self.tablet_power_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)
        self.restart_tablet_button = ttk.Button(self.tablet_power_frame, image=self.restart_tablet_image,
                                                command=self.restart_tablet)
        self.restart_tablet_button.pack(side=LEFT, expand=True, fill=BOTH, padx=150, pady=10)
        self.stop_tablet_button = ttk.Button(self.tablet_power_frame, image=self.stop_tablet_image,
                                             command=self.stop_tablet)
        self.stop_tablet_button.pack(side=LEFT, expand=True, fill=BOTH, padx=150, pady=10)

        # Add tab to root Window
        self.tab_notebook.add(self.app_tab_frame, text='Application')

        # Management Tab
        self.management_tab_frame = ttk.Frame(self.tab_notebook, width=1200, heigh=600)
        self.management_tab_frame.pack()

        # Header Management Frame
        self.header_management_tab_frame = ttk.LabelFrame(self.management_tab_frame,
                                                          text="Monitoring and Administtration",
                                                          style="Blue.TLabelframe")
        self.header_management_tab_frame.config(relief=RIDGE)
        self.header_management_tab_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)
        ttk.Label(self.header_management_tab_frame, image=self.settings_image).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.header_management_tab_frame, text='Manage your tablet !').grid(row=1, column=1)

        # Devices status Frame
        self.devices_status_frame = ttk.LabelFrame(self.management_tab_frame, text="Devices Status",
                                                   style="Blue.TLabelframe")
        self.devices_status_frame.config(relief=RIDGE)
        self.devices_status_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)

        self.devices_status_lcd_image = ttk.Label(self.devices_status_frame, image=self.devices_status_red_lcd_image)
        self.devices_status_lcd_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_barcode_image = ttk.Label(self.devices_status_frame,
                                                      image=self.devices_status_red_barcode_image)
        self.devices_status_barcode_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_gsm_image = ttk.Label(self.devices_status_frame, image=self.devices_status_red_gsm_image)
        #self.devices_status_gsm_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_pyweb_image = ttk.Label(self.devices_status_frame,
                                                    image=self.devices_status_red_pyweb_image)
        self.devices_status_pyweb_image.pack(side=LEFT, expand=True, fill=BOTH)
        self.devices_status_filesystem_image = ttk.Label(self.devices_status_frame,
                                                         image=self.devices_status_red_filesystem_image)
        self.devices_status_filesystem_image.pack(side=LEFT, expand=True, fill=BOTH)

        self.devices_status_printer_image = ttk.Label(self.devices_status_frame,
                                                         image=self.devices_status_red_printer_image)
        self.devices_status_printer_image.pack(side=LEFT, expand=True, fill=BOTH)

        self.devices_status_usb_key_image = ttk.Label(self.devices_status_frame,
                                                      image=self.devices_status_red_usb_key_image)
        #self.devices_status_usb_key_image.pack(side=LEFT, expand=True, fill=BOTH)

        self.devices_status_recheck_button = ttk.Button(self.devices_status_frame,
                                                        image=self.devices_status_recheck_image,
                                                        command=self.status_recheck)

        self.devices_status_recheck_button.pack(side=LEFT, expand=True, fill=BOTH)

        # Management Support Frame
        self.support_frame = ttk.LabelFrame(self.management_tab_frame, text="Support", style="Blue.TLabelframe")
        self.support_frame.config(relief=RIDGE)
        self.support_frame.pack(side=TOP, expand=True, fill=BOTH, padx=10, pady=10)

        self.support_admin_access_button = ttk.Button(self.support_frame, image=self.support_admin_access_image,
                                                      command=lambda: self.admin_access(master))
        self.support_admin_access_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_remote_access_button = ttk.Button(self.support_frame, image=self.support_remote_access_image,
                                                       command=self.remote_access)
        self.support_remote_access_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_remote_access_button.state(['disabled']) # We disable the button at the start to let recheck function to change it if needed, this is for test only
        self.support_contact_button = ttk.Button(self.support_frame, image=self.support_contact_image,
                                                 command=self.support_contact)
        self.support_contact_button.pack(side=LEFT, expand=True, fill=BOTH)
        self.support_backup_button = ttk.Button(self.support_frame, image=self.support_red_backup_image, command=self.support_backup)
        #self.support_backup_button.pack(side=LEFT, expand=True, fill=BOTH)

        # Progressbar for remote access button
        self.progressbar_remote_access = ttk.Progressbar(self.support_frame, orient = HORIZONTAL, length = 200)
        self.progressbar_remote_access.config(mode = 'indeterminate')

        # Add tab to root Window
        self.tab_notebook.add(self.management_tab_frame, text='Management and Settings')

    def restart_tablet(self):
        result = messagebox.askyesno(title='Restart Tablet', message='Do you want to restart tablet ?',
                                     icon="warning")
        customize_desktop_pid = "/tmp/desktop_customize_desktp_pid"
        if result == True:
            bashCommand = "/bin/bash /home/pi/custum_desktop/arret_relance_tablette/relance_tablette.sh"
            os.system(bashCommand)
            if os.path.exists(customize_desktop_pid) and os.path.getsize(customize_desktop_pid) > 0:
                messagebox.showerror(title='Restart Tablet', message='Restart Tablet error', icon="error")
                # self.stop_app_button.state(['!disabled'])
            else:
                messagebox.showinfo("Restart Tablet", "The tablet will restart", icon="info")
                # self.stop_app_button.state(['disabled'])
        # print(messagebox.askyesno(title='restart tablet', message='Do you want to restart the tablet ?',  icon="warning"))
        print("restart_tablet")

    def stop_tablet(self):
        result = messagebox.askyesno(title='Stop Tablet', message='Do you want to shutdown the tablet ?',
                                     icon="warning")
        customize_desktop_pid = "/tmp/desktop_customize_desktp_pid"
        if result == True:
            bashCommand = "/bin/bash /home/pi/custum_desktop/arret_relance_tablette/arret_tablette.sh"
            os.system(bashCommand)
            if os.path.exists(customize_desktop_pid) and os.path.getsize(customize_desktop_pid) > 0:
                messagebox.showerror(title='Stop Tablet', message='Shutdown Tablet error', icon="error")
                # self.stop_app_button.state(['!disabled'])
            else:
                messagebox.showinfo("Stop Tablet", "The tablet will shutdown", icon="info")
                # self.stop_app_button.state(['disabled'])
        # print(messagebox.askyesno(title='restart tablet', message='Do you want to shutdown the tablet ?', icon="warning"))
        print("stop_tablet")

    def start_nativefier(self):
        self.stop_app_button.state(['!disabled'])
        odoo_pid = "/tmp/odoo_pid"
        bashCommand = "/bin/bash /home/pi/custum_desktop/acces_admin/test_odoo_pid.sh"
        os.system(bashCommand)
        answer_odoo_pid = open('/home/pi/custum_desktop/logs/odoo.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/odoo.txt")
        if os.path.exists(odoo_pid) and os.path.getsize(odoo_pid) > 0 and answer_odoo_pid == 'OK':
            bashCommand = "/bin/bash /home/pi/nativefier/MobileIT/put_odoo_in_front.sh"
            os.system(bashCommand)
        else:
            bashCommand = "/bin/bash /home/pi/nativefier/MobileIT/mobile-it.sh"
            os.system(bashCommand)
        self.status_app_image.configure(image=self.green_circle_image)
        print("start_nativefier")

    def stop_nativefier(self):
        result = messagebox.askyesno(title='stop application', message='Do you want to shutdown the application ?',
                                     icon="warning")
        odoo_pid = "/tmp/odoo_pid"
        if result == True:
            bashCommand = "/bin/bash /home/pi/nativefier/MobileIT/mobile-it_stop.sh"
            os.system(bashCommand)
            if os.path.exists(odoo_pid) and os.path.getsize(odoo_pid) > 0:
                messagebox.showerror(title='stop application', message='Shutdown application error', icon="error")
                self.stop_app_button.state(['!disabled'])
            else:
                messagebox.showinfo("stop application", "The application has stopped", icon="info")
                self.stop_app_button.state(['disabled'])
                self.status_app_image.configure(image=self.red_circle_image)

        # print(messagebox.askyesno(title='stop Application', message='Do you want to stop application ?',  icon="warning"))
        print("stop_nativefier")

    def status_recheck(self):
        result = messagebox.askyesno(title='Check peripheral devices', message='Do you want the peripheral check status ?',
                                     icon="warning")
        if result == True:
            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_barcode.sh"
            os.system(bashCommand)
            answer_barcode = open('/home/pi/custum_desktop/logs/check_barcode.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_barcode.txt")
            if answer_barcode == 'OK':
                self.devices_status_barcode_image.configure(image=self.devices_status_green_barcode_image)
            else:
                self.devices_status_barcode_image.configure(image=self.devices_status_red_barcode_image)

            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_lcd.sh"
            os.system(bashCommand)
            answer_lcd = open('/home/pi/custum_desktop/logs/check_lcd.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_lcd.txt")
            if answer_lcd == 'OK':
                self.devices_status_lcd_image.configure(image=self.devices_status_green_lcd_image)
            else:
                self.devices_status_lcd_image.configure(image=self.devices_status_red_lcd_image)

            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_pywebdriver.sh"
            os.system(bashCommand)
            answer_pyweb = open('/home/pi/custum_desktop/logs/check_pyweb.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_pyweb.txt")
            if answer_pyweb == 'OK':
                self.devices_status_pyweb_image.configure(image=self.devices_status_green_pyweb_image)
            else:
                self.devices_status_pyweb_image.configure(image=self.devices_status_red_pyweb_image)

            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_internet.sh"
            os.system(bashCommand)
            answer_gsm = open('/home/pi/custum_desktop/logs/internet_test.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/internet_test.txt")
            if answer_gsm == 'OK' :
                self.devices_status_gsm_image.configure(image=self.devices_status_green_gsm_image)
                self.support_remote_access_button.state(['!disabled'])
            else :
                self.devices_status_gsm_image.configure(image=self.devices_status_red_gsm_image)
                self.support_remote_access_button.state(['disabled'])


            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_filesystem.sh"
            os.system(bashCommand)
            answer_filesystem = open('/home/pi/custum_desktop/logs/check_filesystem.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_filesystem.txt")
            if answer_filesystem == 'OK':
                self.devices_status_filesystem_image.configure(image=self.devices_status_green_filesystem_image)
            else:
                self.devices_status_filesystem_image.configure(image=self.devices_status_red_filesystem_image)

            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_printer.sh"
            os.system(bashCommand)
            answer_printer = open('/home/pi/custum_desktop/logs/check_printer.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_printer.txt")
            if answer_printer == 'OK':
                self.devices_status_printer_image.configure(image=self.devices_status_green_printer_image)
            else:
                self.devices_status_printer_image.configure(image=self.devices_status_red_printer_image)

            bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_usb_key.sh"
            os.system(bashCommand)
            answer_usb_key = open('/home/pi/custum_desktop/logs/check_usb_key.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/check_usb_key.txt")
            if answer_usb_key == 'OK':
                self.devices_status_usb_key_image.configure(image=self.devices_status_green_usb_key_image)
            else:
                self.devices_status_usb_key_image.configure(image=self.devices_status_red_usb_key_image)

            messagebox.showinfo("Check peripheral devices", "Check operation is end! \n"
                                                            "Please contact the support for any red square",
                                icon="info")

            print("status_recheck")

    def status_recheck_no_button(self):
        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_barcode.sh"
        os.system(bashCommand)
        answer_barcode = open('/home/pi/custum_desktop/logs/check_barcode.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_barcode.txt")
        if answer_barcode == 'OK':
            self.devices_status_barcode_image.configure(image=self.devices_status_green_barcode_image)
        else:
            self.devices_status_barcode_image.configure(image=self.devices_status_red_barcode_image)

        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_lcd.sh"
        os.system(bashCommand)
        answer_lcd = open('/home/pi/custum_desktop/logs/check_lcd.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_lcd.txt")
        if answer_lcd == 'OK':
            self.devices_status_lcd_image.configure(image=self.devices_status_green_lcd_image)
        else:
            self.devices_status_lcd_image.configure(image=self.devices_status_red_lcd_image)

        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_pywebdriver.sh"
        os.system(bashCommand)
        answer_pyweb = open('/home/pi/custum_desktop/logs/check_pyweb.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_pyweb.txt")
        if answer_pyweb == 'OK':
            self.devices_status_pyweb_image.configure(image=self.devices_status_green_pyweb_image)
        else:
            self.devices_status_pyweb_image.configure(image=self.devices_status_red_pyweb_image)

        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_internet.sh"
        os.system(bashCommand)
        answer_gsm = open('/home/pi/custum_desktop/logs/internet_test.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/internet_test.txt")
        if answer_gsm == 'OK' :
            self.devices_status_gsm_image.configure(image=self.devices_status_green_gsm_image)
            self.support_remote_access_button.state(['!disabled'])
        else :
            self.devices_status_gsm_image.configure(image=self.devices_status_red_gsm_image)
            self.support_remote_access_button.state(['disabled'])


        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_filesystem.sh"
        os.system(bashCommand)
        answer_filesystem = open('/home/pi/custum_desktop/logs/check_filesystem.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_filesystem.txt")
        if answer_filesystem == 'OK':
            self.devices_status_filesystem_image.configure(image=self.devices_status_green_filesystem_image)
        else:
            self.devices_status_filesystem_image.configure(image=self.devices_status_red_filesystem_image)

        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_printer.sh"
        os.system(bashCommand)
        answer_printer = open('/home/pi/custum_desktop/logs/check_printer.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_printer.txt")
        if answer_printer == 'OK':
            self.devices_status_printer_image.configure(image=self.devices_status_green_printer_image)
        else:
            self.devices_status_printer_image.configure(image=self.devices_status_red_printer_image)

        bashCommand = "/bin/bash /home/pi/custum_desktop/check_module/check_usb_key.sh"
        os.system(bashCommand)
        answer_usb_key = open('/home/pi/custum_desktop/logs/check_usb_key.txt', 'r').read().rstrip('\n')
        os.remove("/home/pi/custum_desktop/logs/check_usb_key.txt")
        if answer_usb_key == 'OK':
            self.devices_status_usb_key_image.configure(image=self.devices_status_green_usb_key_image)
        else:
            self.devices_status_usb_key_image.configure(image=self.devices_status_red_usb_key_image)

        print("status_recheck")


    def admin_access(self, master):

        def try_login(window, master):
            print("Trying to login...")
            arglist = ' ' + username_guess.get() + ' ' + password_guess.get()
            bashCommand = "/bin/bash /home/pi/custum_desktop/acces_admin/authentication.sh" + arglist
            os.system(bashCommand)
            answer_authentication = open('/home/pi/custum_desktop/logs/authentication.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/authentication.txt")
            print(answer_authentication)
            if answer_authentication == 'OK':
                messagebox.showinfo("-- COMPLETE --", "You Have Now Logged In. \n"
                                                    "The Customize Desktop will be closed !", icon="info")
                window.destroy()
                master.destroy()
                os.remove("/tmp/desktop_customize_desktp_id")
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
        attempt_login = ttk.Button(window, text="Login", command=lambda: try_login(window, master))

        username_text.pack()
        username_guess.pack()
        password_text.pack()
        password_guess.pack()
        attempt_login.pack()
        # Main Starter
        window.mainloop()

        print("admin_access")

    # Function to connect to VPN via GSM modem
    def remote_access(self):
        result = messagebox.askyesno(title='Remote access', message='Do you want to enable remote access ? \n'
                                                                    'Make sure the support are ready to proceed ! ',icon="info")
        if result == True:
            #self.progressbar_remote_access.pack()
            #self.progressbar_remote_access.start()
            bashCommand = "/bin/bash /home/pi/custum_desktop/remote_access/connect_to_vpn_box.sh"
            os.system(bashCommand)
            #self.progressbar_remote_access.stop()
            answer_vpn = open('/home/pi/custum_desktop/logs/vpn_answer.txt', 'r').read().rstrip('\n')
            os.remove("/home/pi/custum_desktop/logs/vpn_answer.txt")
            if answer_vpn == 'OK':
                messagebox.showinfo("Support Access", "The Support operator can access the tablet", icon="info")
                self.support_remote_access_button.state(['disabled'])
            else:
                messagebox.showerror(title='Support Access', message='There may and error \n'
                                                                     'Please Contact Support using  support information contact', icon="error")
                self.support_remote_access_button.state(['!disabled'])

        print("remote_access")

    def support_contact(self):
        message = ['Tel : +237 000000000', 'Facebook : facebook/mobileITPOS', 'whatsapp : +237 000000000',
                   'Email : mobileitafrica@gmail.com']
        messagebox.showinfo(title='MobileIT POS', message="\n".join(message), icon="info")
        print("support_contact")

    # Function to display time dynamically
    def update_timeText(self):
        # Get the current time, note you can change the format as you wish
        current = time.strftime("%Y-%m-%d %H:%M:%S")
        # Update the timeText Label box with the current time
        self.timeText.configure(text=current)
        # Call the update_timeText() function after 1 second
        self.master.after(1000, self.update_timeText)

    # Cron job to call refresh button : THis section enable to refresh the state of all the connected devices on tablet
    def cron_check_device_status(self):
        custom_desktop_pid = "/tmp/desktop_customize_desktp_id"
        if os.path.exists(custom_desktop_pid) and os.path.getsize(custom_desktop_pid) > 0:
            threading.Timer(3600.0, self.cron_check_device_status).start() # the time is in second
            self.status_recheck_no_button()

    def support_backup(self):
        result = messagebox.askyesno(title='Backup Tablet', message='Do you want to backup tablet  ?\n'
                                                                    'Make sure that you do not currently use app',
                                     icon="warning")
        if result == True:
            bashCommand = "/bin/bash /home/pi/custum_desktop/remote_access/backup_usb_key.sh"
            os.system(bashCommand)
            answer_backup = open('/home/pi/custum_desktop/logs/backup_answer.txt', 'r').read().rstrip('\n')
            if answer_backup == 'OK':
                messagebox.showinfo("Backup Tablet", "Backup was successfully made", icon="info")
                self.support_backup_button.configure(image=self.support_green_backup_image)
            elif answer_backup == 'KO' :
                messagebox.showerror(title='Backup Tablet', message='An error occur during Backup', icon="error")
                self.support_backup_button.configure(image=self.support_red_backup_image)
            elif answer_backup == 'KOO' :
                messagebox.showerror(title='Backup Tablet', message='Not enough space on the drive \n'
                                                                    'Please contact support', icon="error")
                self.support_backup_button.configure(image=self.support_red_backup_image)

        print("Backup Tablet")

def main():
    root = Tk()
    root.geometry('{}x{}'.format(1024, 600))
    pointofsale = PointOfSale(root)
    pointofsale.update_timeText()
    pointofsale.cron_check_device_status()
    root.attributes("-fullscreen", True)
    root.mainloop()


if __name__ == "__main__": main()
