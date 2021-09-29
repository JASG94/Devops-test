import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

returned_data = {"hello" : "world"} 

@app.route('/', methods=['GET'])
def home():
    return "Only avilable endpoint is /helloworld"

@app.route('/helloworld', methods=['GET'])
def api_all():
    return flask.jsonify(returned_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


app.run()