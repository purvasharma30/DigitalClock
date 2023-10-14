# Import the necessary modules from the tkinter library
from tkinter import Label, Tk
import time

# Create the main application window
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1, 1)

# Define font and styling for the digital clock
text_font = ("Boulder", 68, 'bold')
background = "#b18ced"
foreground = "#6e6d6a"
border_width = 25

# Create a Label widget for displaying the digital clock
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# Define a function to update the digital clock
def digital_clock():
    # Get the current time in the "Hour:Minute:Second" format
    time_live = time.strftime("%H:%M:%S")
    
    # Update the label's text with the current time
    label.config(text=time_live)
    
    # Schedule the digital_clock function to run every 200 milliseconds
    label.after(200, digital_clock)

# Start the digital clock
digital_clock()

# Start the main application loop
app_window.mainloop()
