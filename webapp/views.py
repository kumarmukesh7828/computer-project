from django.shortcuts import render,redirect
from webapp.models import Computer
from webapp.forms import ComputerForm,ComputerSearchForm
from webapp.admin import ComputerAdmin
from django.shortcuts import get_object_or_404

# Create your views here.

def index_view_page(request):
    title = "Computer Information Management System "
    context = {
        "title":title,
    }
    return render(request,'myapp/index.html',context)

def Home_page_view(request):
    title = "welcome to the home page"
    context = {
        "title":title,
    }
    return render(request,'myapp/home.html',context)



def computer_entry(request):
    title = "Add Computer"
    form = ComputerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/computerlist')
    context = {
        "title":title,
        "form":form,
    }
    return render(request,'myapp/computer_entry.html',context)

def computer_list(request):
    title = "List of All Computer"
    queryset = Computer.objects.all()
    form = ComputerSearchForm(request.POST or None)
    context = {
        "title":title,
        "queryset":queryset,
        "form":form,
    }
    if request.method == 'POST':
        queryset = Computer.objects.all().order_by('-timestamp').filter(computer_name__icontains=form['computer_name'].value(),user_name__icontains=form['user_name'].value())
        context = {
            "title":title,
            "queryset":queryset,
            "form":form,

        }
    return render(request,'myapp/computer_list.html',context)

def computer_edit(request,id=None):
    instance = get_object_or_404(Computer,id=id)
    form = ComputerForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/computerlist')
    context = {
        "title":'Edit'+str(instance.computer_name),
        'instance':instance,
        'form':form,

    }
    return render(request,'myapp/computer_entry.html',context)

def computer_delete(request,id=None):
    instance = get_object_or_404(Computer,id=id)
    instance.delete()
    return redirect('/computerlist')