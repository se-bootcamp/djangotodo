from django.shortcuts import render
from .models import Todolistbl
# Create your views here.


def index(request):
    todo_tasks=Todolistbl.objects.order_by('id')
    context={'todo_tasks':todo_tasks}
    return render(request,'lists/index.html',context)