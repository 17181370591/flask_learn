from flask import Flask,request,current_app,make_response,redirect,abort
from flask_script import Manager

app = Flask(__name__)
manager=Manager(app)


@app.route('/')
def index():
    header=request.headers      #请求，请求header类似字典
    #header['test']=233     会报错，environheaders不能修改
    print('current_app.name=',current_app.name)  #输出hello
    print('app.app_content()=',app.app_context())   
    return '<h1>网吧{}</h1>'.format(header)   #输出整个header

@app.route('/user/<name>')      
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/red/<name>')      
def red(name):
    return redirect('/uu')      #访问/red/.*?会重定向访问/uu

@app.route('/u') 
def u():
    resp=make_response('<h1>傻逼 !</h1>')
    resp.set_cookie('shabi','only you')     #设置cookie
    return resp

@app.route('/uu') 
def uu():
    return '<h1>傻逼aaa</h1>',404     #返回404错误，打印傻逼aaa

@app.route('/abort/<user>')
def abortuser(user):
    if len(user)<3:
        abort(404)
    return '<h1>hello {}</h1>'.format(user)   

if __name__ == '__main__':
    manager.run()
##    app.run()
