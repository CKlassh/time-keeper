"""
Title   :   Time Keeper
Author  :   Cameron Schweeder
Date    :   2020.03.29
Time    :   1H:40M
"""
from tkinter import *
import time
from datetime import datetime



root = Tk()
root.title("Time Keeper")
root.geometry("300x200")
root.configure(bg='#363434')
root.resizable(width=False, height=False)

def update_clock():
    """
    Creates a clock feature that displays the current time on the widgit
    """
    now = time.strftime("%H:%M:%S")
    timeLabel.configure(text=now)
    timeLabel.after(1000, update_clock)

def time_Keeper(start, end):
    """
    Function takes in a start time, and end time, and returns the difference
    Input   :   str : A time string in 24H format 13:30 = 1:30PM
    Output  :   str : A string of text representing the time elapsed
    """
    startHour, startMinute = start.split(":")
    endHour, endMinute = end.split(":")
    startHour   = int(startHour)
    startMinute = int(startMinute)
    endHour     = int(endHour)
    endMinute   = int(endMinute)

    if startHour > endHour:
        endHour += 24
    
    start = startHour * 60 + startMinute
    end = endHour * 60 + endMinute

    totalHours = int((end - start)/60)
    totalMinutes = (end - start)%60

    if totalMinutes < 10:
        totalMinutes = str(totalMinutes).zfill(2)

    return str(totalHours) +":" + str(totalMinutes)


def clicked(value, value1):
    """
    Creates Time stamp for log.txt
    Get's the values from 2 input fields and passes them to time_Keeper()
    Returns a label with the output from time_Keeper and adds an entry to log.txt
    ----
    Input   : str   : Value, Value2 assumes in ##:##, ##:## format
    Output  : None
    """
    ansLabel = Label(frame, text="Time Spent"+ time_Keeper(value, value1), bg="#5c5757")
    ansLabel.grid(row=3, column=1)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date = now.strftime("%Y-%M-%d")
    f = open('timelog.csv','a')
    f.write(str(date) + ",Programming,"+inputStart.get()+","+ inputEnd.get()+ ',' + time_Keeper(value, value1) +"\n")
    f.close

# Pack a frame to center the app
frame = LabelFrame(root, bg="#5c5757", text="Enter Start and End Time", pady=20, padx=10)
frame.pack(padx=20, pady=20)

#Label "Start Time[HH:MM]"
startLabel = Label(frame, text="Start Time[HH:MM]", bg="#5c5757")
startLabel.grid(row=0, column=0)

# Input Field Beside Start Time Label
inputStart = Entry(frame, width=20, bg="#efecec")
inputStart.grid(row=0, column=1)

# Label "End Time"
endLabel = Label(frame, text="End Time[HH:MM]", bg="#5c5757")
endLabel.grid(row=1, column=0)

# Input Field Beside End Time Label
inputEnd = Entry(frame, width=20, bg="#efecec")
inputEnd.grid(row=1, column=1)

# Label displaying "Current Time is" then changes to display spent time after function call
ansLabel = Label(frame, text="Current Time is: ", bg="#5c5757")
ansLabel.grid(row=3, column=1)

# Submit button
ansButton = Button(frame, text="Execute", bg="#62929a", command=lambda: clicked(str(inputStart.get()), str(inputEnd.get())))
ansButton.grid(row=3, column=0)

# Time Stamp Label Displaying the current time.
timeLabel = Label(frame, bg="#5c5757")
timeLabel.grid(row=4, column=1)




# Main loop to keep graphical window open
update_clock()
root.mainloop()