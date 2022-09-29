from django.shortcuts import render, redirect
from .models import Todos

# Create your views here.


def index(request):
    todos = Todos.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def new(request):
    return render(request, "todos/new.html")


def detail(request, pk_):

    todo = Todos.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }
    return render(request, "todos/detail.html", context)


def edit(request, pk_):
    # get 메소드를 사용해서 특정 pk 데이터를 불러온다.
    todo = Todos.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }

    return render(request, "todos/edit.html", context)


def create(request):
    todos = Todos.objects.all()
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    Todos.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )

    context = {
        "todos": todos,
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }

    return redirect("todos:index")


def update(request, pk):

    todo = Todos.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todos:index")


def delete(request, pk):
    Todos.objects.get(id=pk).delete()

    return redirect("todos:index")
