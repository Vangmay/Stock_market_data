
import yfinance as yf
import plotly.graph_objs as go
from tkinter import *
import psutil
root = Tk()
root.geometry('700x500')
#entry boxes
entry_frame = Frame(root,bg = "#cfcfe2" ,height =700,width = '800')
entry_frame.pack(pady = 180)

ticker_entry = Entry(entry_frame,text = "Please enter ticker",width = 50, )
ticker_entry.pack()
ticker_entry.insert(0,'enter ticker name')

start_entry = Entry(entry_frame,text = "enter start date",width = 50)
start_entry.pack()
start_entry.insert(0,'enter start date in yy-mm-dd')

end_entry = Entry(entry_frame,text = "Please enter end date",width = 50)
end_entry.pack()
end_entry.insert(0,'enter end date in yy-mm-dd')

interval_entry = Entry(entry_frame,text = "Please enter interval",width = 50)
interval_entry.pack()
interval_entry.insert(0,'enter interval in (d) days')

period_entry = Entry(entry_frame,text = "Please enter period",width = 50)
period_entry.pack()
period_entry.insert(0,'enter period')
#entry boxes finish
#variables
ticker = ticker_entry.get
def input_ticker():
    global ticker 
    ticker = ticker_entry.get()
    stat = yf.download(tickers = ticker,start=start_entry.get(),end = end_entry.get(),interval = interval_entry.get(),period = period_entry.get())
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=stat.index,
    open=stat['Open'],
    high = stat['High'],
    low = stat['Low'],
    close= stat['Close'],name = 'market data'))
    fig.update_layout(
        title = ticker +' share price',
        yaxis_title ='Stock price (USD PER SHARE)')
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)   
    fig.show()
ticker_btn = Button(entry_frame,text = "Submit details",command = input_ticker,)
ticker_btn.pack()
root.mainloop()