import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/first_api',methods=['POST'])
def first_api():
    
    print('started')
    
    data=request.json['data']
    
    print(data)
    
    return jsonify('I am happy to build my first api.'+'This is what you passed'+ str(data))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/internal_api',methods=['POST'])
def first__internal_api():
    
    print('started')
    
    data=[x for x in request.form.values()]
    
    print(data)
    
    return render_template('home.html',output='Hey I am happy. Its, working see your input: '+str(data))


if __name__=='__main__':
    app.run(debug=True)

