from django.shortcuts import render, redirect
from tasks.models import User
from tasks.forms import LoginForm


def index(request):
    if "user_id" not in request.session:
        return redirect("login-page")

    return render(request, "task_index.html")


def visitor_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = User.objects.get_or_create(**form.cleaned_data)[0]
            request.session["user_id"] = user.id
            return redirect("tasks-page")

    context = {
        "form": form,
    }

    return render(request, "login.html", context)
