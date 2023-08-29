import tkinter as tk
import time
from plyer import notification
import json
import os


# functions section
def add_reminder():
    addr = tk.Tk()
    addr.minsize(height=400, width=400)

    def set_function():
        reminder_code = remindercode_entry.get()
        # global event_name 
        event_name = eventname_entry.get()
        event_time = eventtime_entry.get()
        data_dict = {reminder_code: [event_name, event_time]}
        remindercode_entry.delete(0, "end")
        eventname_entry.delete(0, "end")
        eventtime_entry.delete(0, "end")
        f1 = open("reminderdatastore.txt", "a+")
        f1.write(json.dumps(data_dict))
        a = "\n"
        f1.write(a)
        f1.close()

    eventname_label = tk.Label(addr, text="Event Name", width=25)
    eventname_entry = tk.Entry(addr, width=25)
    eventtime_label = tk.Label(addr, text="Event Time", width=25)
    eventtime_entry = tk.Entry(addr, width=25)
    remindercode_label = tk.Label(addr, text="Reminder Code", width=25)
    remindercode_entry = tk.Entry(addr, width=25)
    set_button = tk.Button(addr, text="SET", width=15, command=set_function)
    exit_button = tk.Button(addr, text="Exit", width=15, command=addr.destroy)
    remindercode_label.pack()
    remindercode_entry.pack()
    eventname_label.pack()
    eventname_entry.pack()
    eventtime_label.pack()
    eventtime_entry.pack()
    remindercode_label.pack()
    remindercode_entry.pack()
    set_button.pack()
    exit_button.pack()


def delete_reminder():
    delr = tk.Tk()
    delr.minsize(height=400, width=400)

    def delete_function():
        is_skipped = False
        current_index = 0
        reminder_code = remindercode_entry.get()
        original_file = "reminderdatastore.txt"
        dummy_file = original_file + '.bak'
        # Open original file in read only mode and dummy file in write mode
        with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
            # Line by line copy data from original file to dummy file
            for line in read_obj:
                a = json.loads(line)
                # If current line number matches the given line number then skip copying
                if reminder_code not in a:
                    write_obj.write(line)
                else:
                    is_skipped = True
                current_index += 1
        # If any line is skipped then rename dummy file as original file
        if is_skipped:
            os.remove(original_file)
            os.rename(dummy_file, original_file)
        else:
            os.remove(dummy_file)
        remindercode_entry.delete(0, "end")
        #     def onClick():
    #     tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")

    remindercode_label = tk.Label(delr, text="Enter Reminder Code", width=25)
    remindercode_entry = tk.Entry(delr, width=25)
    delete_button = tk.Button(delr, text="Delete", width=10, command=delete_function)
    exit_button = tk.Button(delr, text="Exit", width=10, command=delr.destroy)
    remindercode_label.pack()
    remindercode_entry.pack()
    delete_button.pack()
    exit_button.pack()


def getting_time():
    rem_code = 0
    f3 = open("reminderdatastore.txt", "r")
    list1 = []
    for i in f3:
        a = json.loads(i)
        list1 = list1 + list(a.keys())
    f2 = open("reminderdatastore.txt", "r")
    for j in f2:
        b = json.loads(j)
        if list1[0] in b:
            rem_code = b[list1[0]][1]
    return rem_code

# main program

def display_notification():
    reminder_code = getting_time()
    current_time = time.strftime("%H:%M:%S")
    
    if reminder_code == current_time:
        notification.notify(
            title="Reminder",
            message="Please Drink Water Now!",
            timeout=12,
            ticker="Hello coder",
            app_name="Python3"
        )
        return True  # Return True if notification is displayed

    return False 


if __name__ == '__main__':
    root = tk.Tk()
    root.minsize(height=400, width=400)
    projectname_label = tk.Label(root, text="APP NAME", width=15)
    showreminder = tk.Label(root, text="Show Reminder", width=15)
    showreminder.pack()
    # while adding name of the font remove spaces it will not accept it.
    projectname_label.pack()
    addreminder_button = tk.Button(root, text="Add Reminder", width=15, command=add_reminder)
    addreminder_button.pack()
    deletereminder_button = tk.Button(root, text="DeleteReminder", width=15, command=delete_reminder)
    deletereminder_button.pack()
    exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
    exit_button.pack()
    root.mainloop()
    reminder_code = getting_time()
    test = 0
    while test == 0:
        currenttime_hour = time.strftime("%H")
        currenttime_minute = time.strftime("%M")
        currenttime_seconds = time.strftime("%S")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        # print(current_time)
        if reminder_code[0:2:1] == currenttime_hour and reminder_code[2:4:1] == currenttime_minute and reminder_code[4:6:1] == currenttime_seconds:
            notification.notify(
                        # title="**Please Drink Water Now!!",
                        
                        message="Drink some water",
                        timeout=12,
                        ticker='Hello',
                        app_name="Reminder app"
            )
            # print("Time ok ")
            # displayNotification()
            test = 1
