from django.contrib import admin
from .models import Ememergy, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(max_length=20000, widget=CKEditorUploadingWidget)
    class Meta:
        model = Ememergy
        fields = '__all__'

class EmemergyAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ("id", "content", "category", "title", "created_at", "update_at", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'content','category', 'photo')
    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)

admin.site.register(Ememergy,EmemergyAdmin)

admin.site.register(Category,CategoryAdmin)
