from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddForm, UserRegisterForm, UserLoginForm, ContactForm
from django.http import HttpResponse
from .models import Ememergy, Category
from  django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.db import models



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.error(request, 'Чувак, тебе фартануло! Ты зарехуестрировался.')
            return redirect('home')
        else:
            messages.error(request,'Ты дурак шоле,!? Нормально зарехуестрируйся!!!!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'ememergy/register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ты дурак шоле,!? Нормально отзовись!!!!')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'ememergy/login.html', {'form':form})


class HomeEmemergy(ListView):
    model = Ememergy
    template_name = 'ememergy/home_ememergy_list.html'
    context_object_name = 'ememergy'
    #extra_context = {'title':'Все про хуету'}
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная дрочь'
        #context['content'] =
        return context

    def get_queryset(self):
        return Ememergy.objects.filter(is_published=True).select_related('category')

class EmemergyByCategory(ListView):
    model = Ememergy
    template_name = 'ememergy/home_ememergy_list.html'
    context_object_name = 'ememergy'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Ememergy.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

class ViewEmemergy(DetailView):
    model = Ememergy
    template_name = 'ememergy/ememergy_detail.html'
    #pk_url_kwarg = 'ememergy_id'

class CreateDroch(LoginRequiredMixin, CreateView):
    form_class = AddForm
    template_name = 'ememergy/add_droch.html'
    login_url = '/admin/'

def send_message(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],form.cleaned_data['content'], '0639584089@ukr.net',['tsss81@ukr.net','0939913558@ukr.net'], fail_silently=False)
            if mail:
                messages.error(request, 'Малява запузырена.')
                return redirect('home')
            else:
                    messages.error(request, 'Ты чаво фуфло толкаешь тут?!')
        else:
            messages.error(request, 'Ты дурак шоле,!? Нормально зарехуестрируйся!!!!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'ememergy/send_message.html', {'form': form})



#def index(request):
    #ememergy = Ememergy.objects.all()
    #context = {
        #'ememergy':ememergy,
           # }
    r#eturn render(request, 'ememergy/index.html', context=context)

#def get_category(request, category_id):
   #ememergy = Ememergy.objects.filter(category_id=category_id)
   #category = Category.objects.get(pk=category_id)
   #return render(request, 'ememergy/category.html', {'ememergy':ememergy,'category':category})

#def view_ememergy(request, ememergy_id):
    #ememergy_item = get_object_or_404(Ememergy,pk=ememergy_id)
    #ememergy_item = Ememergy.objects.get(pk=ememergy_id)
    #return render(request, 'ememergy/view_ememergy.html', {'ememergy_item':ememergy_item})

#def add_droch (request):
    #if request.method == 'POST':
        #form = AddForm(request.POST)
        #if form.is_valid():
            #print(form.cleaned_data)
            #ememergy = Ememergy.objects.create(**form.cleaned_data)
            #ememergy =form.save()
            #return redirect(ememergy)
    #else:
        #form = AddForm()
    #return render (request, 'ememergy/add_droch.html',{'form':form})