import time, sys
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

def pick():
    result = askcolor(title='Simple Color Chooser by crckturtle')
    print('RGB', result[0])
    print('HEX', result[1])

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text='Dummy Window (don\'t close)').grid(column=0, row=0)
ttk.Label(frm, text='made by crckturtle with Tkinter').grid(column=0, row=1)

print('Offline Color Chooser by crckturtle')
time.sleep(1)
print('Use "pick" in console to bring up the menu again\n')
time.sleep(3)

while True:
    pick()
    user_input = input('\n')
    if user_input.strip().lower() == 'exit':
        sys.quit
        break
    elif user_input.strip().lower() != 'pick':
        print('\nInvalid input. Type "pick" to open the color chooser again, or "exit" to quit.\n')

root.mainloop()
