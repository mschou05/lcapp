from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods= ['GET','POST'])
def index():
  	#return render_template('index.html')
  	if request.method=='GET':
  		return render_template('index.html')
		#return render_template('userinfo_schou.html')
	else:
		return render_template('index.html')
		#app_schou.vars['stock'] = request.form['stock_schou']
		#return redirect('/main')	

if __name__ == '__main__':
  app.run(port=33507)
