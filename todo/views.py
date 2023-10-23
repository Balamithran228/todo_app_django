from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, TaskForm
from django.contrib import messages
from .models import Task


from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa

def home(request):
    name = request.user
    tasks = Task.objects.filter(user=name)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.user = name
            info.save()
        return redirect('todo')
    return render(request, 'todo.html', {'tasks': tasks, 'form': form})

def update(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('todo')

    return render(request, 'update.html', {"form":form})

def delete(request,pk):
    data = Task.objects.get(id=pk)
    data.delete()
    return redirect('todo')

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "account was created sucessfuly for"+user)
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.info(request, ' USERNAME or PASSWORD IS INCORRECT')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def render_pdf_view(request):
    pass
    """
    template_path = 'profile.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return redirect('todo')
    return response
    """










