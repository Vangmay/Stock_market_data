import finplot as fplt
import yfinance as yf
from tkinter import *
root = Tk()
root.geometry('800x500')
#ENTRY BOXES
Ticker_entry = Entry(root)
Ticker_entry.pack()
Ticker_entry.insert(0,'Enter ticker')
Start_entry = Entry(root)
Start_entry.pack()
Start_entry.insert(0,'Enter Start date')
End_entry = Entry(root)
End_entry.pack()
End_entry.insert(0,'Enter End date')
Period_entry = Entry(root)
Period_entry.pack()
Period_entry.insert(0,'Enter Period')
Interval_entry = Entry(root)
Interval_entry.pack()
Interval_entry.insert(0,'Enter Interval')
#ENTRY BOXES
def input_ticker():
    stats = yf.download(tickers=Ticker_entry.get(),start = Start_entry.get(),end = End_entry.get(),period = Period_entry.get(),interval=Interval_entry.get())
    fplt.candlestick_ochl(stats[['Open','High','Low','Close']])
    fplt.show()
#making button
btn = Button(root,text = 'submit',command=input_ticker)
btn.pack()
root.mainloop()