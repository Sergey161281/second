from django.db import models
from django.urls import reverse
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Create your models here.

class Ememergy(models.Model):
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField( blank=True, verbose_name='Дрочь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='ФОТО', blank=True)
    is_published = models. BooleanField(default=True, verbose_name='Запузырено')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def  get_absolute_url(self):
         return reverse('view_ememergy', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id":self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']




