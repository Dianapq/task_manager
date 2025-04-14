# Listar tareas
def list_tasks():
    if not list_tasks:
        print("📭 No hay tareas.")
        return
    for idx, task in enumerate(list_tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{idx}. {task['description']} [{status}] - ID: {task['id']}")