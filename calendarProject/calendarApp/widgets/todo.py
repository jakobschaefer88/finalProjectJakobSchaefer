from .base import BaseWidget

class TodoWidget(BaseWidget):
    name = 'todo'
    template_name = "calendarApp/widgets/todo.html"

    _tasks = []
    _completed_tasks = []

    def add_task(self, task):
        """Add a new task."""
        self._tasks.append({"task": task, "completed": False})

    def mark_task_completed(self, task_index):
        """Mark a task as completed."""
        if 0 <= task_index < len(self._tasks):
            self._tasks[task_index]["completed"] = True
            self._completed_tasks.append(self._tasks[task_index])
            del self._tasks[task_index]  # Remove the task from the active list

    def delete_task(self, task_index):
        """Delete a task."""
        if 0 <= task_index < len(self._tasks):
            del self._tasks[task_index]

    def get_context_data(self, user=None, config=None):
        return {
            "tasks": self._tasks,
            "completed_tasks": self._completed_tasks
        }
