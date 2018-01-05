from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,DateTimeField,RadioField
from wtforms import BooleanField,SubmitField,validators 
from flask_bootstrap import Bootstrap
import datetime

app=Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='secret key'

class MyForm(FlaskForm):
    field1=StringField('username',[validators.Required()])
    field2=PasswordField('password',[validators.Required()])

    field6=SubmitField('Submit')
    
    
@app.route('/b')
def b():

    return render_template('b.html',title='b')

    
@app.route('/')
def index():
    oldcon=session.get('con')
    session['con']=None
    print(oldcon)
    return render_template('index.html',title='Index',con=oldcon)

@app.route('/login',methods=['GET','POST'])
def login():
    myform=MyForm()    
    if request.method=='POST':
        flash('old:{}'.format(session['user']))
        session['user']=myform.field1.data
        flash('new:{}'.format(session['user']))
        session['con']=myform.field1.data
        return redirect(url_for('index'))
    return render_template('login.html',title='login',myform=myform)


if __name__=='__main__':
    app.run(port=5000)
'''

{% extends "bootstrap/base.html" %} 
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}
{% block content %}
<div class="container">
    <div class="page-header">
        <h1>Hello, {{ name }}!</h1>
    </div>
</div>
{% endblock %}
'''
