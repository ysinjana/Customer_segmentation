import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('cust_seg.pkl','rb'))

with open('bins_function.pkl', 'rb') as file:
    stored_function = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    
    data1=np.array(list(data.values())) #.reshape(1,-1)
    print(data)
    print(data1[0])
    new_data=[]
    new_data[0:2]=stored_function([data1[0]],[data1[1]],[data1[2]])
    y2= [val for sublist in new_data for val in sublist]
    #print(y2)
    
    output=model.predict([y2])
    print(output)
    op=output.tolist()
    '''
    return jsonify(output[0])
    '''
    return jsonify(op)
@app.route('/predict',methods=['POST'])

def predict():
   
    data1=[int(x) for x in request.form.values()]
    new_data=[]
    new_data[0:2]=stored_function([data1[0]],[data1[1]],[data1[2]])
    y2= [val for sublist in new_data for val in sublist]
    print(y2)
    
    output=model.predict([y2])[0]
    if output==0:
        oname="Power Shoppers"
    elif output==1:
        oname="Loyal Customers"
    elif output==2:
        oname="At-risk Customers"
    else:
        oname="Recent Customers"
    print(oname)
    return render_template("home.html",prediction_text="Type of Customer is : {}".format(oname))

if __name__=="__main__":
    app.run(debug=True)