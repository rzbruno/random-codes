import os
from bottle import route, request, static_file, run

@route('/')
def root():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
           Select a file: <input type="file" name="upload" />
           <input type="submit" value="Start upload" />
        </form>'''

@route('/upload', method='POST')
def do_upload():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.zip'):
        return "File extension not allowed."

    save_path = "/tmp/"

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    return "File successfully saved to '{0}'.".format(save_path)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
