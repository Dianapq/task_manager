def mark_task_as_completed(task_list, task_id):
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return "Task not found"
