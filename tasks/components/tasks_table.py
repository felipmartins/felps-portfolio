from django_unicorn.components import UnicornView
from tasks.models import Task, User
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "is_completed"]


class TasksTableView(UnicornView):
    form_class = TaskForm
    errors = {}
    title = ""
    description = ""
    user_id = None
    is_completed = False
    tasks = Task.objects.none()

    def mount(self):
        self.user_id = self.request.session.get("user_id")
        self.load_table()

    def load_table(self):
        self.tasks = Task.objects.all()

    def clear(self):
        self.title = ""
        self.description = ""
        self.is_completed = False

    def add_task(self):
        self.errors = self.validate()
        if not self.errors:
            user = User.objects.get(id=self.user_id)

            Task.objects.create(
                title=self.title,
                description=self.description,
                is_completed=self.is_completed,
                user=user,
            )
            self.clear()

        self.load_table()
