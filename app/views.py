from django.shortcuts import render, redirect
from .forms import DataForm
from django.contrib import messages
from .models import UserFrom


# Create your views here.

def index(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request Completed')
            return redirect('app:home')
        return render(request, 'pages/home.html')
    else:
        form = DataForm()
        content = {
            'title': 'CrudApp::Home',
            'form': form,
            'data': UserFrom.objects.all(),
        }
        return render(request, 'pages/home.html', content)


def edit_view(request, id):
    data_edited = UserFrom.objects.get(id=id)
    if request.method == 'POST':
        data_edited.name = request.POST['name']
        data_edited.email = request.POST['email']
        data_edited.subject = request.POST['subject']
        data_edited.message = request.POST['message']
        data_edited.save()
        messages.success(request, "Data Updated Successfully")
        return redirect("app:home")
    else:
        return render(request, 'pages/edit.html', {'data': data_edited})


def delete_view(request, id):
    data_object = UserFrom.objects.get(id=id).delete()
    if data_object:
        messages.info(request, "Deleted Successfully")
        return redirect("app:home")


def select_view(request, id):
    read_data = UserFrom.objects.get(id=id)
    if read_data:
        content = {'selected_data': read_data}
        return render(request, "pages/data.html", content)
