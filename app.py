from flask import Flask,render_template,request
import pandas as pd
from psaw import PushshiftAPI
import datetime as dt
import time
from collections import Counter
from itertools import zip_longest
import pandas as pd
from datetime import date
from datetime import timedelta
import functools, operator
import os



app = Flask(__name__)

@app.route('/')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
 

         filename = dt.datetime.today().strftime("%d %m %Y")+".csv"
     
         data = pd.read_csv(filename)
        
         currname=[]
         counts=[]
         for i in data.values:
            #print(i)
            if i[1] != 0:
                currname.append(i[0])
                counts.append(i[1])
        
        # print(currname)
        # print(counts)
         dictionary = dict(zip(currname, counts))   
         #print(dictionary)

         return render_template('index.html',dict=dictionary)

@app.route('/yesterday', methods=['GET','POST'])
def yesterday():
    if request.method == 'GET':
        Previous_Date = dt.datetime.today() - dt.timedelta(days=1)
        Previous_Date_Formatted = Previous_Date.strftime("%d %m %Y")
        
        filename = Previous_Date_Formatted +'.csv'
        data = pd.read_csv(filename)
        
        currname=[]
        counts=[]
        for i in data.values:
            #print(i)
            if i[1] != 0:
                currname.append(i[0])
                counts.append(i[1])
        
        # print(currname)
        # print(counts)
        dictionary = dict(zip(currname, counts))   
         #print(dictionary)

        return render_template('yesterday.html',dict=dictionary)

 

if __name__ == '__main__':
    app.run(debug=True)