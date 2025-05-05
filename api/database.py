

tasks = [
    {"id": 1, "title": "Faire les courses", "completed": False, "person": "Alice"},
    {"id": 2, "title": "Coder l'app React", "completed": True, "person": "Bob"},
    {"id": 3, "title": "Écrire la documentation", "completed": False, "person": "Alice"},
    {"id": 4, "title": "Préparer le repas", "completed": True, "person": "Charlie"}
]

def get_tasks_by_person(person):
    return [task for task in tasks if task["person"].lower() == person.lower()]
