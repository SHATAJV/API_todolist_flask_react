from flask import request, jsonify
from database import tasks

# GET /tasks
def get_all_tasks():
    return jsonify(tasks)

# POST /tasks
def add_task():
    new_task = request.get_json()
    new_task['id'] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

# GET /tasks/{person}
def get_tasks_by_person(person):
    filtered_tasks = [t for t in tasks if t['assigned_to'].lower() == person.lower()]
    return jsonify(filtered_tasks)
