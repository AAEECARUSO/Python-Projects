

import pyautogui
import subprocess
from time import sleep
from datetime import datetime as dt


##################################################################################
#   GLOBAL VARIABLES
##################################################################################
present = False
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
my_class_paths["CHEM 105"] = "C:/path/to/script_with_zoom_url/CHEM_105.vbs"
my_class_paths["CSE 280"] = "C:/path/to/script_with_zoom_url/CSE280.vbs"

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
my_classes_times["CHEM 105"] = [ (14, 0), (15, 0) ]  # 2:00 -> 3:00
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


def alert(name, starting):
    global minutes_early

    if starting:
        message = "{} Class Will Begin In {} Minutes".format(name, minutes_early)
        print(message)
    else:
        message = "{} Class Has Ended".format(name)
        print(message)


def time():
    current = str(dt.now())
    current = current.split()
    current = current[1].split(":")
    hour = int(current[0])
    minute = int(current[1])

    if hour > 12:
        hour2 = hour - 12
        time = str(hour2) + ":" + str(minute) + " PM"

    elif hour == 12:
        time = str(hour) + ":" + str(minute) + " PM"

    else:
        time = str(hour) + ":" + str(minute) + " AM"

    return(time, hour, minute)


def start_class(path):
    global present

    subprocess.call([path], shell=True)
    # The Code Above Starts A VBS Script Which Opens
    # A Web-browser And Goes To The Zoom Classroom Link

    sleep(15)

    pyautogui.press('left')
    sleep(2)
    pyautogui.press('enter')

    sleep(60)

    pyautogui.keyDown('winleft')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('r')

    pyautogui.keyUp('r')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('winleft')
    # The Code Above Starts Our Screen And Voice Recording
    # Using A Hotkey Combination

    present = True


def end_class():
    global present

    pyautogui.keyDown('winleft')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('r')

    pyautogui.keyUp('r')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('winleft')
    # The Code Above Ends Our Screen And Voice Recording

    pyautogui.keyDown('alt')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    pyautogui.keyUp('alt')

    sleep(3)
    # The Code Above Leaves The Meeting

    present = False


try:
    while(True):
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
                    alert(class_name, True)
                    start_class(mcp)

            elif current_hour == end_h and current_minute >= end_m:
                if day_of_week in mcd and present and class_name == class_in_session:
                    alert(class_name, False)
                    end_class()

        sleep(60)

except Exception as e:
    e = str(e)
    print("Class Bot Encountered Error\n{}".format(e))
    print("{}".format(e))
