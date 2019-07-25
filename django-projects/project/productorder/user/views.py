from django.shortcuts import render
from django.shortcuts import redirect
from .models import User
from .forms import UserForm
from .forms import LoginForm

# Create your views here.
def register_user(request):
    if request.method =="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("login_user")

    else:
        form=UserForm()
    return render(request,"register_user.html",{"form":form})  

def login_user(request):
    if request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form=LoginForm()
    return render(request, "login_user.html",{"form":form})     
                                    

def list_users(request):
    users = User.objects.all()
    return render(request,"list_users.html",{"users":users})


def edit_user(request,pk):
    user=User.objects.get(pk=pk)
    if request.method == "POST":
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
    else:
        form=UserForm(instance=user)
    return render(request,"edit_user.html",{"form":form})           


# def edit_user(request,pk):
#     user=User.objects.get(pk=pk)
#     if request.method == "POST":
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserForm(instance=user) 
#     return render(request,"edit_user.html",{"form":form})           
   # email = request.POST['email']
        # first_character = email[0]

        # if int(first_characher):
        #     error = "first character must be an alphabet"
        #     return render(request,"register_user.html", {"error":error})

        # user = User.objects.get() 
