# Generated by Django 3.1.3 on 2020-11-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pochta_main', '0007_billing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileresult',
            name='accuracy',
            field=models.CharField(blank=True, max_length=3, verbose_name='Код точности'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_A',
            field=models.CharField(blank=True, max_length=100, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_B',
            field=models.IntegerField(blank=True, default=0, verbose_name='Строение'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_BOX',
            field=models.IntegerField(blank=True, default=0, verbose_name='Абонентский ящик'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_C',
            field=models.CharField(blank=True, max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_D',
            field=models.CharField(blank=True, max_length=2, verbose_name='Дробь'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_E',
            field=models.IntegerField(blank=True, default=0, verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_F',
            field=models.IntegerField(blank=True, default=0, verbose_name='Помещение'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_N',
            field=models.IntegerField(blank=True, default=0, verbose_name='Номер дома'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_NL',
            field=models.CharField(blank=True, max_length=2, verbose_name='Литера'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_P',
            field=models.CharField(blank=True, max_length=100, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_R',
            field=models.CharField(blank=True, max_length=100, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_S',
            field=models.CharField(blank=True, max_length=100, verbose_name='Улично-дорожные элементы'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_T',
            field=models.CharField(blank=True, max_length=100, verbose_name='Внутригородская территория'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='field_index',
            field=models.CharField(blank=True, max_length=6, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='file_source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pochta_main.fileparse'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='ident_low',
            field=models.CharField(blank=True, max_length=50, verbose_name='Идентификатор нижнего уровня'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='latitude',
            field=models.CharField(blank=True, max_length=10, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='longtitude',
            field=models.CharField(blank=True, max_length=10, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='not_recognize',
            field=models.CharField(blank=True, max_length=5, verbose_name='Полученный адрес'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='num_dest_post',
            field=models.IntegerField(blank=True, default=0, verbose_name='Номер участка'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='source_index',
            field=models.CharField(blank=True, max_length=6, verbose_name='Исходный индекс'),
        ),
        migrations.AlterField(
            model_name='fileresult',
            name='time_answer',
            field=models.IntegerField(blank=True, default=0, verbose_name='Время ответа'),
        ),
    ]
