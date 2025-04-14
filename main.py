# main.py

from createTask import create_task

# Lista vacía para almacenar tareas
task_list = []

descripcion = input("Ingresa la descripción de la tarea: ")
nueva_tarea = create_task(task_list, descripcion)

print("Tarea creada:")
print(f"id: {nueva_tarea['id']}")
print(f"description: {nueva_tarea['description']}")
print(f"completed: {nueva_tarea['completed']}")
