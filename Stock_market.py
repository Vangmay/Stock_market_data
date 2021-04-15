import yfinance as yf
import plotly.graph_objs as go
import psutil
import re
from tkinter import *
import tkinter
from tkinter import messagebox 
from tkinter import Menu

#home page gui
root = Tk()
root.title('Stock Market Data')
root.geometry('800x500')
#home page gui


#Opens "current" window
def current_win():
    current_window = Toplevel(root)
    current_window.geometry('800x500')
    current_window.title('Stock market Live')
    def window_switch():
        current_window.destroy()
        root.deiconify()
    btn = Button(current_window,text='Back',command = window_switch)
    btn.pack(side=tkinter.BOTTOM,padx = 50)
    #current stock market data retriever__________________________________________________________________________________________________________________________________________________
    
    #entry boxes
    entry_frame = Frame(current_window,bg = "#cfcfe2" ,height =700,width = '800')
    entry_frame.pack(pady = 180)

    ticker_entry = Entry(entry_frame,width = 50, )
    ticker_entry.pack()
    ticker_entry.insert(0,'enter ticker name')

    start_entry = Entry(entry_frame,width = 50)
    start_entry.pack()
    start_entry.insert(0,'enter start date in yyyy-mm-dd')

    end_entry = Entry(entry_frame,width = 50)
    end_entry.pack()
    end_entry.insert(0,'enter end date in yyyy-mm-dd')

    interval_entry = Entry(entry_frame,width = 50)
    interval_entry.pack()
    interval_entry.insert(0,'enter interval in (m,minutes or d,days)')

    #entry boxes finish
    #error box
    menuBar = Menu(current_window)
    current_window.config(menu=menuBar)
    def _msgBox(): 
        messagebox.showerror("Error",'Please enter correct format of date in yyyy-mm-dd')
        infoMenu=Menu(menuBar,tearoff=0)
        infoMenu.add_command(command = _msgBox)
    def _msgBoxticker(): 
        messagebox.showerror("Error",'Ticker not found,please check if you have written it correctly')
        infoMenu=Menu(menuBar,tearoff=0)
        infoMenu.add_command(command = _msgBoxticker)
    #variables
    def input_ticker():
        global ticker 
        ticker = ticker_entry.get()
        pattern = r'\d{4}-\d{2}-\d{2}'
        match_start = re.match(pattern,start_entry.get())
        match_end = re.match(pattern,end_entry.get())
        match_start_result = bool(match_start)
        match_end_result = bool(match_end)
        if match_start_result == False or match_end_result == False:
            print('Please enter the correct format of date yyyy-mm-dd')
            _msgBox()
        else:
        
            stat = yf.download(tickers = ticker.upper(),start=start_entry.get(),end = end_entry.get(),interval = interval_entry.get())
            if stat.empty == True:
                _msgBoxticker()
            else:
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=stat.index,
                open=stat['Open'],
                high = stat['High'],
                low = stat['Low'],
                close= stat['Close'],name = 'market data'))
                fig.update_layout(
                    title = ticker.upper() +' share price',
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
#current stock market data retriever______________________________________________________________________________________________________________________________________________

    root.withdraw()

#Opens "history" window
def history_win():
    hist_window = Toplevel(root)
    hist_window.geometry('800x500')
    hist_window.title('Stock market history')
    def window_switch():
        hist_window.destroy()
        root.deiconify()
    btn = Button(hist_window,text='Back',command = window_switch)
    btn.pack(side=tkinter.BOTTOM,padx = 50)
    #Stock market history______________________________________________________________________________________________________________________________________________________
    entry_frame = Frame(hist_window,bg = "#cfcfe2" ,height =700,width = '800')
    entry_frame.pack(pady = 180)
    #entry boxes
    ticker_entry = Entry(entry_frame,width=50)
    ticker_entry.pack()
    ticker_entry.insert(0,'Enter ticker')

    period_entry = Entry(entry_frame,width=50)
    period_entry.pack()
    period_entry.insert(0,'Enter period(y,mo,max)')
    #_______________________________________________________
    #functions
    menuBar = Menu(hist_window)
    hist_window.config(menu=menuBar)
    def _msgBoxticker(): 
        messagebox.showerror("Error",'Ticker not found,please check if you have written it correctly')
        infoMenu=Menu(menuBar,tearoff=0)
        infoMenu.add_command(command = _msgBoxticker)
    def submit():
        ticker = ticker_entry.get()
        stat = yf.download(tickers = ticker.upper(),period=period_entry.get())
        if stat.empty == True:
            _msgBoxticker()
        else:
            fig = go.Figure()
            fig.add_trace(go.Candlestick(x=stat.index,
            open=stat['Open'],
            high = stat['High'],
            low = stat['Low'],
            close= stat['Close'],name = 'market data'))
            fig.update_layout(
                title = ticker.upper() +"'s history of share price",
                yaxis_title ='Stock price (USD PER SHARE)')
            fig.update_xaxes(
            rangeslider_visible=True
        )   
            fig.show()
    #_____________________________________________________________________________________
    #button
    submit_btn = Button(entry_frame,text='Submit',command = submit)
    submit_btn.pack()
    #Stock market history______________________________________________________________________________________________________________________________________________________
    root.withdraw()








#home page gui
button_frame = Frame(root)
button_frame.pack(pady=200,padx=120)
Current_btn = Button(button_frame,text='Current',command = current_win)
Current_btn.pack()
History_btn = Button(button_frame,text='History',command=history_win)
History_btn.pack()
root.mainloop()
#home page gui