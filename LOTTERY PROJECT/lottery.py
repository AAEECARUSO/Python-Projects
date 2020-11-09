

import os                        # needed for checking if file exists
import csv, random
from tkinter import *            # for everything else
from tkinter import messagebox   # for message popups
from tkinter import simpledialog # for getting inputs


def flip_number():

    # 'w+' means opening file in 'write' mode 
    # and create file if it does not exist
    # already. 'w' mode deletes all data in the
    # file upon opening
    with open('lottery.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(1000):
            num = random.randint(1, 1000000)
            writer.writerow([num])

    messagebox.showinfo("Success!", "Lottery pool created!")


def lottery_select():
    # check to see if the file exists in the directory
    if not os.path.exists('lottery.csv'):
        messagebox.showwarning("Error!", "Sorry, we couldn't open a valid lottery numbers file.")
        return
    
    guess = simpledialog.askinteger("Play", "Enter your number:", minvalue = 1, maxvalue = 1000000)

    with open('lottery.csv', "r", newline='') as csvfile: # 'r' means open the file in 'read' mode
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            # csv row needs to be converted from string to int
            if guess == int(row[0]):

                # if the remainder is 0 then it is divisiable
                if guess%7 == 0:
                    messagebox.showinfo("WOW!!!", "Jackpot! You win $5000!")
                else:
                    messagebox.showinfo("Congratulations!", "You win $100!")
                return

        messagebox.showinfo("Sorry...", "You didn't win... Play again sometime soon.")


root = Tk()
root.title("Random")
root.geometry("400x100")

flip_button = Button(root, text = "Create Lotto Pool", command = flip_number)
flip_button.configure(bg = "thistle1")
flip_button.pack()
root.configure(bg = "skyblue1")

roll_button = Button(root, text = "Play Lottery", command = lottery_select)
roll_button.configure(bg = "coral1")
roll_button.pack()

root.mainloop()







