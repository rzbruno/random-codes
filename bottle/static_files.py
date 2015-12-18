from bottle import static_file, run, route, template
import os

path = input("Enter with the path base: ")

files = [f for f in os.listdir(path) if os.path.isfile(path+'/'+f)]

@route('/')
def static():
    return template('''
        <table border="1">
           %for row in rows:
              <tr><a href=/static/{{row}}>{{row}}</a><tr><br>
           %end
        </table>''', rows=files)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=path, download=filename)

run(host='0.0.0.0', port=8080)
