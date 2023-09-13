'''from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!!"

if __name__ == "__main__":
    app.run(debug = True)'''

from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1, 
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    { 'id': 2, 
        'title': u'Study Python',
        'description': u'You need to learn Flask framework',
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hi world"

@app.route("/get-data")
def get_data():
    return jsonify({
        'data' : tasks
    })
   
@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "Please provide the data"
        })
    
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description'),
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully.."
    })


if __name__== "__main__":
    app.run(debug=True)
