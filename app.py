from flask import Flask, render_template, request, redirect, jsonify
import pickle
import numpy as np
#from sklearn.pipeline import Pipeline
#from sklearn.linear_model import LinearRegression
import warnings

warnings.filterwarnings("ignore",category=DeprecationWarning)


app = Flask(__name__)
@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    x = np.array([1.,8.,34.24,38.5])
    f=open('simpleLoanModelLR','r')
    mdl_ = pickle.load(f)
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=mdl_.predict(x)[0])

@app.route('/_return_grades')
def return_grades():
    """Add two numbers server side, ridiculous but well..."""
    
    return jsonify(result='Your ideal loan range is: A - B',
                  chars = 'Important characteristics in this range include: Debt to Income Ratio, Revolving Balance Utilized',
                  returns ='Average returns: 4.7%',
                  details_paid = '94% of loans in this range paid in full',
                  details_loss = '4% of loans in this range had negative returns ')


@app.route('/')
def main():
    return redirect('/index')

@app.route('/index',methods= ['GET','POST'])
def index():
  	#return render_template('index.html')
    
    if request.method=='GET':
        return render_template('index_carto.html')
        #return render_template('userinfo_schou.html')
    else:
        return render_template('index_carto.html')
        #app_schou.vars['stock'] = request.form['stock_schou']
        #return redirect('/main')	

if __name__ == '__main__':
    app.run(port=33507)

def getData(x):
    f=open('simpleLoanModelLR','r')
    mdl_ = pickle.load(f)
    return mdl_.predict(x)[0]
    
