from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm#, AuthenicationForm
# from django.contrib.auth import login
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenicationForm(data=request.POST)
#         if form.is_valid():
#             #log in the User
#             user = form.grt_user()
#             return redirect('articles:list')
#             login(request.user)
#     else:
#         form = AuthenicationForm()
#     return render(request, 'accounts/login.html', {'form': form})
