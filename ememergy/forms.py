from django import forms
from .models import Ememergy, Category
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# class AddForm(forms.Form):
    # title = forms.CharField(max_length=150, label="Тема", widget=forms.TextInput(attrs={'class':'form-control'}))
    # content = forms.CharField(label='Хрень нестерпимая', required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    # is_published = forms.BooleanField(label='Запузырено', initial=True)
    # category = forms.ModelChoiceField(empty_label='выбирай ДРОЧЬ', queryset=Category.objects.all(),label='Дрочь бывает разная', widget=forms.Select(attrs={' class':'form-control'}))

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150, label="Чё за базар?", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(max_length=150, label="Вот така малява", widget=forms.Textarea(attrs={'class': 'form-control', 'rows':7}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Паганяло", help_text='не больше 150 буковок, понял???', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Отзовись", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Отзовись еще раз", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label="Паганяло", help_text='не больше 150 буковок, понял???', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Отзовись", widget=forms.PasswordInput(attrs={'class':'form-control'}))


class AddForm(forms.ModelForm):
    class Meta:
        model = Ememergy
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('запузырь нормально, без цифры вначале! дурак штоле!?')
        return title

    def clean_is_published(self):
        is_published = self.cleaned_data['is_published']
        if is_published == False:
            raise ValidationError('а галку кто поставит?')
        return is_published