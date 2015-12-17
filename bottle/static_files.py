import os

from bottle import static_file, run, route, template

path = input("Enter with the path base: ")

files = [f for f in os.listdir(path) if os.path.isfile(path+'/'+f)]

@route('/')
def static():
    return template('list', rows=files)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=path)

run(host='0.0.0.0', port=8080)
