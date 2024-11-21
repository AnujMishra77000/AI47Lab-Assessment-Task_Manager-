from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from .forms import TaskForm,EmailForm
from django.conf import settings
from .utils import send_email_to_user
from django.urls import reverse



#This function helps to land home page where we have user Login
def home(request):
   return render(request, 'home.html',)


#After User signin they will land on This "dashboard" page with the access of View, Delete, Add there task
def Dashboard(request):
   TaskList = Task.objects.all()
   return render(request, 'dashboard.html', {'TaskList':TaskList})

# If user is Admin and signin with there admin credentials then admin will land this function it will check if 
# signedin user is Admin then it will redirects to ADMIN_REDIRECT_URL which gives the path to this admin
# user to continue as admin. this is restricted function.
@login_required
def Post_login(request):
    user = request.user
    if user.is_superuser or user.groups.filter(name='admin').exists():
        # Redirect admin users
        return redirect(settings.ADMIN_REDIRECT_URL)
    else:
        # Redirect regular users
        return redirect(settings.LOGIN_REDIRECT_URL.replace('/postlogin/','/dashboard/'))

#this function implemented to store and give regular user details which are signedin with Googleoauth, to the admin
# this ia restricted function only admin can access and manages the user details     
@login_required
def Admin_Page(request):
    if not request.user.is_superuser:
        # Prevent access for non-admins
        return render(request, 'unauthorized.html')  
    
    # Fetch all social account details
    social_accounts = SocialAccount.objects.select_related('user').all()

    context = {
        'social_accounts': social_accounts
    }
    return render(request, 'google_oauth.html', context)


#The logic behind of this function is Authorized admin user can send invitation mail to new users putting there mailID
@login_required  
def send_email(request):
    if not request.user.is_staff:  
        return render(request, 'access_denied.html')
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            send_email_to_user(email)
            return render(request,'emailsuccess.html')     
    else:
       form = EmailForm()

    return render(request, 'registration_mail.html',{'form':form})

#This function helps signdin user to add there Task with title and task description with help of Task Form.
def Add_Task(request):
  if request.method == 'POST':
     form = TaskForm(request.POST)
     if form.is_valid():
         title = form.cleaned_data['Task_title']
         description = form.cleaned_data['Task_description']
         Tsk=Task(Task_title = title, Task_description = description)
         Tsk.save()
         return HttpResponseRedirect(reverse('dashboard'))
  else:
   form = TaskForm()
  return render(request, 'add_task.html', {'form':form})

#with the help of this function user can update there old task with new title or description.
def Update_Task(request, pk):
    if request.method == 'POST':
       task = Task.objects.get(pk=pk)
       form = TaskForm(request.POST, instance=task)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('dashboard'))
    else:
       task = Task.objects.get(pk=pk)
       form = TaskForm(instance = task)  
    return render(request, 'update_task.html', {'form':form})  
 
#This function helps user to delete there old or achieved task.    
def Delete_Task(request, pk):
     if request.method == 'POST':
        task= Task.objects.get(pk=pk)
        task.delete()
        return HttpResponseRedirect(reverse('dashboard'))