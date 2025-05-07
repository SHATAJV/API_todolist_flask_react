tasks = [
    { 'id': 1, 'title': 'Acheter des légumes', 'assigned_to': 'Ashley', 'completed': False },
    { 'id': 2, 'title': 'Faire du ménage', 'assigned_to': 'Kate', 'completed': True },
    { 'id': 3, 'title': 'Réparer la porte', 'assigned_to': 'Ashley', 'completed': False }
]

next_id = 4

def get_all_tasks():
    return tasks, 200

def get_tasks_by_person(person):
    filtered = [t for t in tasks if t['assigned_to'] == person]
    if not filtered:
        return {'error': f'No tasks found for {person}'}, 404
    return filtered, 200

def add_task(body):
    global next_id
    if 'assigned_to' not in body or 'title' not in body:
        return { 'error': 'Missing fields' }, 400
    body['id'] = next_id
    body['completed'] = body.get('completed', False)
    tasks.append(body)
    next_id += 1
    return body, 201
