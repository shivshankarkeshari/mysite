"""



    redirect and reverse
"""

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse


def to_do_f(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'todo/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("ok")
            return HttpResponseRedirect(reverse('list'))

    context = {'form': form}
    return render(request, 'todo/update_task.html', context)


def deleteTask(request, pk):

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return HttpResponseRedirect(reverse('list'))

    context = {'item': item}
    return render(request, 'todo/delete.html', context)
