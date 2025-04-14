# main.py

# main.py
task_list = []

# Intentar importar funciones individualmente
try:
    from createTask import create_task
except ImportError:
    create_task = None
    print(" Módulo 'create_task' no disponible.")

try:
    from Listar_tareas import list_all_tasks
except ImportError:
    List_All_Tasks = None
    print(" Módulo 'list_all_tasks' no disponible.")

try:
    from markTaskAsCompleted import mark_task_as_completed
except ImportError:
    mark_task_as_completed = None
    print(" Módulo 'mark_task_as_completed' no disponible.")

try:
    from deleteTask import delete_task
except ImportError:
    delete_task = None
    print(" Módulo 'delete_task' no disponible.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            if create_task:
                desc = input("Ingrese la descripción de la tarea: ")
                task = create_task(task_list, desc)
                print("Tarea creada:", task)
            else:
                print(" Función de crear no disponible.")

        elif choice == "2":
            if list_all_tasks:
                list_all_tasks(task_list)
            else:
                print(" Función de listar no disponible.")

        elif choice == "3":
            if mark_task_as_completed:
                task_id = input("Ingrese el ID de la tarea a completar: ")
                result = mark_task_as_completed(task_list, task_id)
                print(result)
            else:
                print(" Función de completar no disponible.")

        elif choice == "4":
            if delete_task:
                task_id = input("Ingrese el ID de la tarea a eliminar: ")
                result = delete_task(task_list, task_id)
                print(result)
            else:
                print(" Función de eliminar no disponible.")

        elif choice == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()