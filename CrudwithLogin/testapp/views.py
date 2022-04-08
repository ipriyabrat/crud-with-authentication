 
from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm


# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def BookRetriveView(request):
    book_list=Book.objects.all()
    return render(request,'testapp/book_list.html',{'book_list':book_list})

class BookListView(ListView):
    model=Book
    
class BookListView1(ListView):
    model=Book
     
    

class BookDetailsView(DetailView):
    model=Book

class BookCeeateView(CreateView):
    model=Book
    fields='__all__'


class BookUpdateView(UpdateView):
    model=Book
    fields='__all__'

class BookDeleteView(DeleteView):
    model=Book
    success_url= reverse_lazy('list')

def logout_view(request):
    return render(request,'testapp/logout.html')

from django.http import HttpResponseRedirect
def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password) #to hash password
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
