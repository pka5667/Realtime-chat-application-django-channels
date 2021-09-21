from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
# USER PROFILE VIEW 
def profileView(request, username):
    user_data = User.objects.filter(username=username)
    if len(user_data) == 0:
        return  HttpResponse('<h1>User with this username do not exist</h1>')
    total_messages = User.objects.filter(chatmessage__user_id=user_data[0].id)
    context = {
        'user': list(user_data)[0],
        'total_messages_sent': (total_messages).count()
    }
    return render(request, 'home/profile.html', context)


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
    else:
        form = UserForm(instance=request.user)

    return render(request, 'home/dashboard.html', {'form': form})
