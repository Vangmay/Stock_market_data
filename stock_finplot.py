import finplot as fplt
import yfinance as yf
from tkinter import *
import re
from tkinter import messagebox 
from tkinter import Menu
root = Tk()
root.geometry('800x500')
#ENTRY BOXES
Ticker_entry = Entry(root,width = 30)
Ticker_entry.pack()
Ticker_entry.insert(0,'Enter ticker')
Start_entry = Entry(root,width = 30)
Start_entry.pack()
Start_entry.insert(0,'Enter Start date(yyyy-mm-dd)')
End_entry = Entry(root,width = 30)
End_entry.pack()
End_entry.insert(0,'Enter End date(yyyy-mm-dd)')
Interval_entry = Entry(root,width = 30)
Interval_entry.pack()
Interval_entry.insert(0,'Enter Interval')
#ENTRY BOXES
#error box
menuBar = Menu(root)
root.config(menu=menuBar)
def _msgBox(): 
    messagebox.showerror("Error",'Please enter correct format of date in yy-mm-dd')
    infoMenu=Menu(menuBar,tearoff=0)
    infoMenu.add_command(command = _msgBox)

def input_ticker():
    pattern = r'\d{4}-\d{2}-\d{2}'
    match_start = re.match(pattern,Start_entry.get())
    match_end = re.match(pattern,End_entry.get())
    match_start_result = bool(match_start)
    match_end_result = bool(match_end)
    if match_start_result == False or match_end_result == False:
        _msgBox()
    else:
        stats = yf.download(tickers=Ticker_entry.get(),start = Start_entry.get(),end = End_entry.get(),interval=Interval_entry.get())
        fplt.candlestick_ochl(stats[['Open','High','Low','Close']])
        fplt.show()
#making button
btn = Button(root,text = 'submit',command=input_ticker)
btn.pack()
root.mainloop()
