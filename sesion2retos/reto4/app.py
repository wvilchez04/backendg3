from flask import Flask

app = Flask(__name__)
departamentos = [
    {'nombre':'Arequipa', 'capital':'Arequipa'},
    {'nombre':'Lima', 'capital':'Lima'},
    {'nombre':'Tacna', 'capital':'Tacna'}
]

@app.route('/departamentos/')
def listarDepartamentos():
    mensaje = 'Departamentos del Peru'
    return {
        'ok': True,
        'content': departamentos,
        'message': mensaje
    }        

if __name__ == '__main__':
    app.run()