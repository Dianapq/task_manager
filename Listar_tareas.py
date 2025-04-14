# Listar tareas
def list_tasks(list_tasks):
    if not list_tasks:
        print("📭 No hay tareas.")
        return
    for idx, task in enumerate(list_tasks, 1):
        status = "completada" if task["completed"] else "no completada"
        print(f"{idx}. {task['description']} [{status}] - ID: {task['id']}")