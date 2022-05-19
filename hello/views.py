from dataclasses import field
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from turtle import title
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Category, Task, Task_art, Task_debate,Task_music,Task_art,Task_vision
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# k
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Category
from .forms import BlogForm
from django.urls import reverse_lazy


 # Import TemplateView
# adding Ali

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.core.mail import send_mail


# Add the two views we have been talking about  all this time :)

class WebpageLoginView(LoginView):
    template_name = 'registration/login.html'



class TaskList(ListView):
     
      model = Task
      redirect_field_name = 'redirect_to'
    

class TaskCreate(CreateView):
   
    model= Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')


class TaskCreateMusic(CreateView):
    model= Task_music
    fields= '__all__'
    success_url = reverse_lazy('task-music')
    

class TaskCreateArt(CreateView):
    model= Task_art
    fields= '__all__'
    success_url = reverse_lazy('task-art')    

class TaskCreateVision(CreateView):
    model= Task_vision
    fields= '__all__'
    success_url = reverse_lazy('task-vision')     

class TaskCreateDebate(CreateView):
    model= Task_debate
    fields= '__all__'
    success_url = reverse_lazy('task-debate')       
    
    
def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        data = {
            'name': name,
            'email': email, 
            'subject': subject, 
            'message': message
        }

        message = '''
        New message: {}

        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'], message, '200103368@stu.sdu.edu.kz', ['bornqazaqi@gmail.com'])

    return render(request, 'hello/task_list.html', {})
    
    
    # adding kamshat
    
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

# Create your views here.


    
    # вввв
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm
from django.views.decorators.csrf import csrf_exempt


    # def home(request):
    # 	return render(request, 'clubs/dombyra.html', {})
def dombyra(request):
    	
    	return render(request, 'clubs/dombyra.html', {})

def music(request):
    	return render(request, 'clubs/music.html', {})

@csrf_exempt
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			if 'dombyraClub' in username:  
				# messages.success(request, ('You Have Been Logged In!'))
				return redirect('add_blog')
			elif 'musicClub' in username:
				return redirect('add_blog')
			elif 'artClub' in username:
				return redirect('add_blog')	
				
			else:
				return redirect('tasks')

		else:
			messages.success(request, ('Сен қателестің'))
			return redirect('login')
	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You Have Registered...'))
			return redirect('dombyra')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'authenticate/register.html', context)





# ddddddddddd
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
	
	context = {'form': form}
	return render(request, 'authenticate/change_password.html', context)


from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hello.models import BlogModel
from .forms import BlogForm
from django.urls import reverse_lazy
# Create your views here.

# class HomeView(ListView):
#     model = BlogModel
#     template_name = 'home.html'

def details(request, blog_id):
    model = BlogModel.objects.filter(id=blog_id)
    return render(request,'blog_detail.html', {'object_list': model})

class AddBlogView(CreateView):
    model = BlogModel
    form_class = BlogForm
    template_name = 'add_blog.html'
    
class AddCategoryView(CreateView):
    model = Category
    # form_class = BlogForm
    template_name = 'add_categoryView.html'
    fields = '__all__'   

    # fields = ('title', 'title_tag', 'user', 'content') 

@csrf_exempt
def create_view(request):
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     title_tag = request.POST.get('title_Tag')
    #     image = request.POST.get('image')
    #     content = request.POST.get('content')
    if checkUser(request):
        return redirect('add_category')
    else:
        messages.success(request, ('Сен клубтын хэды емессің'))
        return redirect('tasks')

def checkUser(request):
    if request.user.is_superuser:
        return True
    else:
        return False

class UpdatePostView(UpdateView): 
    model = BlogModel
    template_name = 'update_blog.html'
    fields = ['title', 'title_tag', 'image', 'content']

class DeleteViewPost(DeleteView): 
    model = BlogModel
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')



class HomeView(ListView): 
    model = BlogModel
    template_name = str = 'home.html'
    ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    

def CategoryView(request, cats): 
    category_posts = BlogModel.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class ArticleDetailView(DetailView): 
    model = BlogModel
    template_name = str = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context








    	
   