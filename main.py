import tkinter as tk
from PIL import ImageTk, Image
from Selenium_GetData import selenium_getdata
from Present_Data import present_data

# Global Definition
image_tk1 = None
image_tk2 = None
image_tk3 = None

# Function to handle button click event
def get_and_present():
    global image_tk1
    global image_tk2
    global image_tk3

    # Get input values from the entry widgets
    username = str(entry1.get())
    password = str(entry2.get())
    startDate = entry3.get()
    endDate = entry4.get()

    print(username)
    print(password)
    print(startDate)
    print(endDate)

    selenium_getdata(username,password,startDate,endDate)
    present_data()

    # Clear Window
    for widget in window.winfo_children():
        widget.destroy()

    # Display the images
    image_tk1 = ImageTk.PhotoImage(Image.open("Outputs/RidesPerMonthHist.png").resize((400, 300)))
    labelMonth = tk.Label(window, image=image_tk1)
    labelMonth.grid(row=0, column=0)

    image_tk2 = ImageTk.PhotoImage(Image.open("Outputs/TimeOfDayHist.jpeg").resize((400, 300)))
    labelTime = tk.Label(window, image=image_tk2)
    labelTime.grid(row=0, column=1)

    image_tk3 = ImageTk.PhotoImage(Image.open("Outputs/RidesDurationsHist.png").resize((400, 300)))
    labelDuration = tk.Label(window, image=image_tk3)
    labelDuration.grid(row=0, column=2)

    # Update the window
    window.update()

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Toronto Bike Share Bike Trip History Presenter")

# Create input labels and entry widgets
label1 = tk.Label(window, text="Login Info, Username:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Login Info, Password:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

label3 = tk.Label(window, text="History Query, Start Date ([YYYY, MM, DD]):")
label3.pack()
entry3 = tk.Entry(window)
entry3.pack()

label4 = tk.Label(window, text="History Query, End Date ([YYYY, MM, DD]):")
label4.pack()
entry4 = tk.Entry(window)
entry4.pack()

# Create a button to trigger the calculation
button = tk.Button(window, text="Begin", command=get_and_present)
button.pack()

# Start the main event loop
window.mainloop()