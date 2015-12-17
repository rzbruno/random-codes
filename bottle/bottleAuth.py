from bottle import run, get, post, request

def check_login(username, password):
   return username=='user' and password=='user'

@get('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Logged in.</p>"
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=8080, debug=True)
