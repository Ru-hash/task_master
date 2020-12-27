from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DeleteView
from .models import Task
from django.contrib.auth.models import User
from .forms import TaskForm

def TaskListView(request):
	object_list = Task.objects.filter(author=request.user)
	cnxt = {
	'object_list' : object_list , 
	}
	return render(request,'tasks/task_list.html',cnxt)

class TaskCreateView(CreateView):
	model = Task
	fields=[
		'title' ,
		'content'
	]
	def form_valid(self,form):
		form.instance.author =self.request.user
		return super().form_valid(form)

class TaskDeleteView(DeleteView):
	model = Task
	success_url = '/tasks/'



def home(request):
	return render(request,'tasks/home.html',{})
