from bottle import route, get,run,template,redirect,response,static_file,error, os, request, app
from beaker.middleware import SessionMiddleware
adminuser = 'admin'
adminpwd = '12345'

@route('/')
def index():
    return redirect('shop')


@route('/staff')
def staff():
    karfa = checkcart()
    qty = len(karfa)
    return template('template/index', qty=qty)

@route('/staff/login', method='post')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username,'---->',password)

    if username == adminuser and password == adminpwd:
        response.set_cookie('account', username, secret='my_secret_code')
        return redirect('/staff/login/restricted')
    else:
        return "Login failed. <br> <a href='/'>Login</a>"

@route('/staff/login/restricted')
def restricted():
    user = request.get_cookie('account', secret='my_secret_code')
    print(user)
    if (user):
        return "restricted area. <br> <a href='/staff/login/signout'>log off</a>"
    else:
        return "You are not logged in. Access denied."

@route('/staff/login/signout')
def signout():
    response.set_cookie('account', "", expires=0)
    user = request.get_cookie('account', secret='my_secret_code')
    print(user)
    return "You have sign off <a href='/'>home</a>"


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./resources')

@route('/shop')
def shop():
    karfa = checkcart()
    qty = len(karfa)
    return template('template/sida1', products=products, qty=qty)

def checkcart():
    session = request.environ.get('beaker.session')
    karfa = []
    for p in products:
        for x in session:
            if p['pid'] == x:
                vara = p
                for l in range(session[x]['value']):
                    karfa.append(vara)
    return karfa


@route('/cart')
def cart():
    session = request.environ.get('beaker.session')
    karfa = []
    summa = 0
    for p in products:
        for x in session:
            if p['pid'] == x:
                vara = p
                for l in range(session[x]['value']):
                    karfa.append(vara)
    for x in karfa:
        summa +=x['price']
    summa = round(summa)
    qty = len(karfa)
    print(karfa)
    return template('template/sida2', karfa=karfa, qty=qty, summa=summa)



@route('/cart/add/<pid>')
def cart_add(pid):
    rasevalue = False
    session = request.environ.get('beaker.session')
    for x in products:
        if str(x['pid'])==str(pid):
            for p in session:
                if x['pid'] == p:
                    rasevalue = True

        print(session)
        print(rasevalue)
        if rasevalue:
            print(session[pid])
            session[pid]['value']+=1
            break

    else:
        for x in products:
            if str(x['pid']) == str(pid):
                session[pid] = {'name':x['name'],'value':1}
    session.save()
    print(session)
    return redirect('/shop')

@route('/cart/del/<pid>')
def cart_del(pid):
    session = request.environ.get('beaker.session')
    for x in products:
        if str(x['pid'])==str(pid):
            if int(session[pid]['value']) > 1:
                session[pid]['value']-=1
            elif int(session[pid]['value']) == 1:
                del session[pid]
    session.save()
    print(session)
    return redirect('/cart')

@route('/cart/remove')
def remove_cart():
    session = request.environ.get('beaker.session')
    session.delete()
    return redirect('/shop')







session_options = {
    'session.type': 'file',
    'session.data_dir':'./data'
}

my_session = SessionMiddleware(app(), session_options)

products = [
    {"pid":"0010", "name": "Iphone X", "price": 139895},
    {"pid":"0011", "name": "Iphone 8", "price": 114985},
    {"pid":"0012", "name": "Iphone 8 plus", "price": 139894},
    {"pid":"0013", "name": "LG G6", "price": 59895},
    {"pid":"0110", "name": "LG V30", "price": 99999},
    {"pid":"0211", "name": "Nokia 3310", "price": 4999},
    {"pid":"0312", "name": "Nokia 8110", "price": 6999},
    {"pid":"0413", "name": "Razer Phone", "price": 72789},
    {"pid":"0510", "name": "Samsung g s9", "price": 111985},
    {"pid":"0611", "name": "Samsung g s9 plus", "price": 122985},
    {"pid":"0712", "name": "Samsung Note 8", "price": 139985},
    {"pid":"0813", "name": "Xperia XZ2", "price": 69999},
]



run(app=my_session, host='localhost', port='8080', debug='True', reloader='True')
