from flask import Flask, render_template, request, redirect, jsonify
import dill
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
    grade = request.args.get('grade', 'A', type=str)
    subgrade = request.args.get('subgrade', '1', type=str)
    dti = request.args.get('dti', 0, type=float)
    revol_util = request.args.get('revol_util', 0, type=float)
    f=open('dillModelsAndEncoders','r')
    try:
        dct= dill.load(f)
    except:
        pass
    f.close()
    mdl_=dct['pipeline']
    encodings=dct['encodings']
    x=[encodings['grade'].transform(grade),encodings['sub_grade'].transform(grade+subgrade),dti,revol_util]
    ret=mdl_.predict(x)[0]-1
    prc_return="{0:.2f}".format(ret*100)+'%'
    return jsonify(result='Your model predicted total return is: '+prc_return,
                  chars = 'Important characteristics in this range include: Debt to Income Ratio, Revolving Balance Utilized',
                  returns ='Average total return for similar: 4.7%',
                  details_paid = '94% of loans in this range paid in full',
                  details_loss = '4% of loans in this range had negative returns ')


@app.route('/')
def main():
    return redirect('/index')

@app.route('/index',methods= ['GET','POST'])
def index():
  	#return render_template('index.html')
    #f=open('dillModelsAndEncoders','r')
    #dct= dill.load(f)
    if request.method=='GET':
        return render_template('index_options.html')
        #return render_template('userinfo_schou.html')
    else:
        return render_template('index_options.html')
        #app_schou.vars['stock'] = request.form['stock_schou']
        #return redirect('/main')	

if __name__ == '__main__':
    app.run(port=33507)

def getData(x):
    f=open('simpleLoanModelLR','r')
    mdl_ = pickle.load(f)
    return mdl_.predict(x)[0]
    
