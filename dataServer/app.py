from flask import Flask, url_for, request, json, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/user/<username>')
def user(username):
    return  'hello %s' % username

@app.route('/id/<int:id>')
def getid(id):
    return 'get %d' % id

@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.args.get('name', 'none'))
    if request.method == 'POST':
        return 'post'
    elif request.method == 'GET':
        return jsonify(username=request.args.get('name', 'nobody'), age=30, location='shanghai')



@app.route('/err/')
def error():
    return 'err'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
