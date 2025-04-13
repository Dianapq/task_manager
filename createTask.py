# task_manager.py

task_id_counter = 1 


def generate_unique_id():
    global task_id_counter
    current_id = task_id_counter
    task_id_counter += 1
    return current_id


def create_task(task_list, task_description):
    new_task = {
        "id": generate_unique_id(),
        "description": task_description,
        "completed": False
    }

    task_list.append(new_task)
    return new_task

