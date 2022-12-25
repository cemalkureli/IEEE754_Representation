from ieee754_method import IEEE754
from tkinter import * 
import tkinter as tk
import time

def ieee754(input,p):
    a = IEEE754(input, p)
    temp_precision={
      0:"Half Precision",
      1:"Single Precision",
      2:"Double Precision",
      3:"Quadruple Precision",
      4: "Octuple Precision"
    }
    temp_str = f"{temp_precision[p]} Representation: {a}\n\n{temp_precision[p]} Hex Representation: {a.str2hex()}"
    return temp_str

def convert_ieee754():

  try:
    if input_entry.get() != "":
      input = float(input_entry.get()) # take input from user
      time.sleep(0.25)
    else:
      time.sleep(0.25)
    if input_entry2.get() != "":
      p = int(input_entry2.get()) # take precision representation type from user
      time.sleep(0.25)
    else:
      time.sleep(0.25)
      # window.destroy() 

    if (0<=p<5):
      ieee754_value = str(ieee754(input,p)) # convert the input to IEEE 754 representation
      result_label.config(text=ieee754_value) # display
      input_entry.delete(0,input_entry.index(tk.END))
      input_entry2.delete(0,input_entry2.index(tk.END))
    
  except:
    time.sleep(0.25)
    result_label.config(text="Wrong Input") # display



    

# create the main window
window = tk.Tk()
window.title("IEEE 754 Converter")

# create Adjust size
window.geometry("800x400")
 
# set minimum window size value
window.minsize(800, 400)
 
# set maximum window size value
window.maxsize(1600, 400)


#  create a label for the input field and create an input field

empty_label = tk.Label(text="IEEE 754 CONVERTER")
empty_label.pack()
empty_label = tk.Label()
empty_label.pack()
input_label = tk.Label(text="Enter Decimal Input")
input_label.pack()
empty_label = tk.Label()
empty_label.pack()
input_entry = tk.Entry()
input_entry.pack()
empty_label = tk.Label()
empty_label.pack(anchor="w")
input_label2 = tk.Label(text="0: Half Precision\n1: Single Precision\n"
                          +"2: Double Precision\n3: Quadruple Precision\n"
                          +"4: Octuple Precision\n\nEnter Precision (0, 1, 2, 3, 4)")
input_label2.pack()
empty_label = tk.Label()
empty_label.pack()
input_entry2 = tk.Entry()
input_entry2.pack()
empty_label = tk.Label()
empty_label.pack()

# create a button for converting the input
convert_button = tk.Button(text="Convert", command=convert_ieee754)
convert_button.pack()

empty_label = tk.Label()
empty_label.pack()

# create a label for displaying the result
result_label = tk.Label(text="")
result_label.pack()

# run the app
window.mainloop()

