from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

tasks = [
    {'id': 1, 'title': 'Acheter des légumes', 'assigned_to': 'Ashley', 'completed': False, 'priority': 'Haute',
     'date': '2025-05-10'},
    {'id': 2, 'title': 'Faire du ménage', 'assigned_to': 'Kate', 'completed': True, 'priority': 'Moyenne',
     'date': '2025-05-05'},
    {'id': 3, 'title': 'Réparer la porte', 'assigned_to': 'Ashley', 'completed': False, 'priority': 'Basse',
     'date': '2025-05-07'}
]


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5176'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
    return response


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data.get('title') or not data.get('assigned_to') or not data.get('priority') or not data.get('date'):
        return jsonify({'message': 'error'}), 400

    new_id = max([task['id'] for task in tasks], default=0) + 1
    new_task = {
        'id': new_id,
        'title': data['title'],
        'assigned_to': data['assigned_to'],
        'completed': False,
        'priority': data['priority'],
        'date': data['date']
    }

    tasks.append(new_task)
    return jsonify(new_task), 201



@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204
@app.route('/tasks/<string:username>', methods=['GET'])
def get_tasks_for_user(username):
    user_tasks = [task for task in tasks if task['assigned_to'].lower() == username.lower()]
    return jsonify(user_tasks), 200


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)

    if not task:
        return jsonify({'message': 'Tâche non trouvée'}), 404

    task['title'] = data.get('title', task['title'])
    task['assigned_to'] = data.get('assigned_to', task['assigned_to'])
    task['priority'] = data.get('priority', task['priority'])
    task['date'] = data.get('date', task['date'])
    task['completed'] = data.get('completed', task['completed'])

    return jsonify(task)


if __name__ == '__main__':
    app.run(debug=True)
