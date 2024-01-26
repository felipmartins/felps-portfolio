from django_unicorn.components import UnicornView


class FilterView(UnicornView):
    search = ""

    def updated_search(self, query):
        self.parent.load_table()

        if query:
            self.parent.tasks = list(self.parent.tasks.filter(title__icontains=query))
