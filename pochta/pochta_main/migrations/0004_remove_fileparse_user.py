# Generated by Django 3.1.3 on 2020-11-14 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pochta_main', '0003_fileparse_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileparse',
            name='user',
        ),
    ]
