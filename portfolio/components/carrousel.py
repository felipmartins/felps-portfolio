from django_unicorn.components import UnicornView
from portfolio.models import Project


class CarrouselView(UnicornView):
    def mount(self):
        self.projects = Project.objects.all()
        self.initial = 0
        self.amount = len(self.projects)

    def next_project(self):
        self.initial += 1
        if self.initial == self.amount:
            self.initial = 0

    def previous_project(self):
        self.initial -= 1
        if self.initial == -1:
            self.initial = self.amount - 1

    def clear_name(self):
        self.projects = ["teste2", "teste3"]
