import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

returned_data = {"hello" : "world"} 

@app.route('/', methods=['GET'])
def home():
    return "Only avilable endopoint is /helloworld"

@app.route('/helloworld', methods=['GET'])
def api_all():
    return flask.jsonify(returned_data)



app.run()