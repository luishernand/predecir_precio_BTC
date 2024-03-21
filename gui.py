import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from tkinter import *

def show_entry():
    pipeline = joblib.load('pipeline')
    
    p1 = float(e1.get())
    p2 = float(e2.get())
    
    
    sample = pd.DataFrame({
   'Open':[p1],
    'Volume':[p2],
    },index=[0])
    
    
    result = pipeline.predict(sample)
    print(result)
    Label(master, text = "Close Prices").grid(row =1)
    Label(master, text = result[0]).grid(row =14)
    
master = Tk()
master.title('Close Prices Prediction using Machine Leanirng')
label  =Label(master, text= 'Close Prices Predictions', bg ='black', fg = 'white').grid(row = 0, columnspan =2)

Label(master, text = "Enter Open Prices").grid(row =1)
Label(master, text = "Enter Volume").grid(row =2)



#clicked = StringVar()
#options = ['male', 'female']

#e1 = OptionMenu(master, clicked, *options)
#e1.configure(width= 15)
e1 = Entry(master)
e2 = Entry(master)


e1.grid(row = 1, column = 1)
e2.grid(row = 2, column = 1)


Button(master, text="Predict", command = show_entry).grid()

mainloop()