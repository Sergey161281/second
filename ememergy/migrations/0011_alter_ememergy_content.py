# Generated by Django 4.0.4 on 2022-06-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ememergy', '0010_alter_ememergy_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ememergy',
            name='content',
            field=models.TextField(blank=True, verbose_name='Дрочь'),
        ),
    ]
