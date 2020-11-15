# Generated by Django 3.1.3 on 2020-11-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileParse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_upload', models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')),
                ('file_path', models.FileField(upload_to='', verbose_name='Файл')),
                ('current_record', models.IntegerField(default=0, editable=False, verbose_name='Текущая запись')),
                ('all_record', models.IntegerField(default=0, editable=False, verbose_name='Всего записей')),
            ],
        ),
    ]