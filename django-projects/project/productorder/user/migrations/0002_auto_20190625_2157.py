# Generated by Django 2.2.2 on 2019-06-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='your_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
