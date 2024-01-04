# import tkinter
#
# window = tkinter.Tk()
# window.title('Miles Calculator')
# window.minsize(width=800, height=600)
# def test(*args):
#     print(type(args))
#     print(args)
#
# test(1,2,1,5)
# # Label
# my_label = tkinter.Label(window, text='Miles')
# my_label.pack()
#
#
#
#
#
#
#
#
#
#
#
# window.mainloop()
#


import tkinter as tk


def miles_to_km():
    try:
        # Get the value entered by the user
        miles = float(entry.get())

        # Perform the conversion
        kilometers = miles * 1.60934

        # Update the result label
        result_label.config(text=f"{miles} miles is {kilometers:.2f} kilometers")
    except ValueError:
        result_label.config(text="Please enter a valid number for miles.")


# Create the main window
root = tk.Tk()
root.title("Miles to Kilometers Converter")
root.minsize(width=500, height=500)

# Create and place widgets
label = tk.Label(root, text="Enter Miles:")
label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=miles_to_km)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()

