



import sys
import sms
import pyautogui
import subprocess
import tkinter as tk
import gettime as gt
from time import sleep

from datetime import datetime as dt


##################################################################################
#   GLOBAL VARIABLES
##################################################################################
present = False
close_window = True # This is the default
message_response = False

minutes_early = 5
class_in_session = str()


weekDays = ("Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday")


##################################################################################
#   This is where you list the names of your classes.
##################################################################################
my_classes = ["CSE 280",
              "CHEM 105"]


##################################################################################
#   This is where you put the path to each of the VBS scripts for your classes.
##################################################################################
my_class_paths = dict()
my_class_paths["CHEM 105"] = "C:/Users/arnhn/Desktop/ALL APPS/CHEM_105.vbs"
my_class_paths["CSE 280"] = "C:/Users/arnhn/Desktop/ALL APPS/CSE280.vbs"


##################################################################################
#   This is where you list the specific days for each of your classes.
##################################################################################
my_classes_days = dict()
my_classes_days["CHEM 105"] = ("Monday", "Tuesday", "Wednesday", "Friday")
my_classes_days["CSE 280"] = ("Tuesday", "Thursday")


##################################################################################
#   This is where you list the specific hour and minute for each of your classes.
#   The first element is the START time and the second element is the END time.
##################################################################################
my_classes_times = dict()
my_classes_times["CHEM 105"] = [ (14, 0), (15, 0) ]    # 2:00 -> 3:00
my_classes_times["CSE 280"] = [ (15, 15), (16, 15) ] # 3:15 -> 4:15


##################################################################################
#   This section will offset our original class start times according
#   to the number of minutes we want to be early to class which can be set
#   by adjusting the "minutes_early" variable at the top of this script.
##################################################################################
for class_name in my_classes:
    mct = my_classes_times.get(class_name)
    start_h = mct[0][0]
    start_m = mct[0][1]
    end_h = mct[1][0]
    end_m = mct[1][1]

    start_m = (start_m - minutes_early)
    if start_m < 0:
        start_h = start_h - 1
        start_m = (60 + start_m)
    my_classes_times[class_name][0] = (start_h, start_m)




def ExitApplication():
    global close_window, message_response

    pyautogui.keyDown('win')
    pyautogui.press('down')
    pyautogui.press('down')
    # DO NOT RELEASE THE WINDOWS KEY YET!!!

    root = tk.Tk()
    timeout = 20000 # milliseconds
    root.after(timeout, root.destroy)

    MsgBox = tk.messagebox.askquestion ('Close Window','YOUR CLASS HAS ENDED. CLOSE OUT OF CURRENT WINDOW?',icon = 'warning')

    if MsgBox == 'yes':
        message_response = True
        close_window = True
        root.destroy()
    elif MsgBox == 'no':
        close_window = False
        root.destroy()




def start_class(path):
    global present
    subprocess.call([path], shell=True)
    present = True




def end_class():
    global present, close_window, message_response

    ExitApplication()

    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.keyUp('win') # NOW THE WINDOWS KEY CAN BE RELEASED!!

    if close_window:

        notepad = pyautogui.locateCenterOnScreen('notepad.png')

        if notepad == None or message_response:
            message_response = False

            sleep(2)
            pyautogui.click()

            pyautogui.keyDown('alt')
            pyautogui.keyDown('f4')
            pyautogui.keyUp('f4')
            pyautogui.keyUp('alt')
            # The Code Above Leaves The Meeting

    # Rest to the default
    close_window = True
    present = False




while(True):

    try:

        the_date = dt.now()
        day_of_week = weekDays[the_date.weekday()]
        datetime_string = str(the_date)
        current_hour, current_minute = gt.time()[1:]

        for class_name in my_classes:
            mcp = my_class_paths.get(class_name)
            mct = my_classes_times.get(class_name)
            mcd = my_classes_days.get(class_name)
            start_h = mct[0][0]
            start_m = mct[0][1]
            end_h = mct[1][0]
            end_m = mct[1][1]

            if current_hour == start_h and current_minute >= start_m:
                if day_of_week in mcd and not present:
                    class_in_session = class_name
                    start_class(mcp)

            elif current_hour == end_h and current_minute >= end_m:
                if day_of_week in mcd and present and class_name == class_in_session:
                    end_class()

    except Exception as e:
        e = str(e)
        sms.send("Class Bot Encountered Error\n{}".format(e))
        sms.send("{}".format(e))

    sleep(60)


























