from django.shortcuts import render, redirect
from tasks.models import Task


def tasks_view(request):
    task = request.GET["task"]
    Task.objects.create(title=task)
    return redirect("/tasks")


def completed_tasks_view(request):

    return render(
        request,
        "completed_tasks.html",
        {"tasks": Task.objects.filter(completed=True, deleted=False)},
    )


def all_tasks_view(request):
    return render(
        request,
        "tasks.html",
        {"tasks": Task.objects.filter(completed=False, deleted=False)},
    )


def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return redirect("/tasks")


def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return redirect("/tasks")
