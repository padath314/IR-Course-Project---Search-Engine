### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def result(score):
    res=""
    return render_template('result.html',result=res)

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        qry=request.form['Type your query here']
    return redirect(url_for('result',score=qry))
  
if __name__=='__main__':
    app.run(debug=True)