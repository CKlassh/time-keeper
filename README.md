# time-keeper
Tkinter app to keep track of time and log it in a csv file


Good tool for keeping track of billable time, or just how much time each project is getting.
Useful for quickly calculating differences between time as well. If you are lazy like me ;-)

When you first start the program. Enter in the current time (Shown on the bottom of app) as [HH:MM]
Then continue working on what ever project you are on. 
When you are ready to take a break, or done for the day enter the current time in the end field as [HH:MM]
Click Execute, and it will update the label with total time spent.


(Optional)
If you want to log the time in a csv file, enter the name of the Project in the first field, and toggle the checkbox to log.
On execute, it will create or update a timelog.csv with format;
[ Date, Project Name, Start Time, End Time, Time Spent ]
