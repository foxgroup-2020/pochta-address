from django.db import models
from django.contrib.auth.models import User
import os

class FileParse(models.Model):
    date_upload = models.DateTimeField('Дата загрузки', auto_now=True)
    file_path = models.FileField('Файл', upload_to='docs/')
    current_record = models.IntegerField('Текущая запись', default=0, editable=False)
    all_record = models.IntegerField('Всего записей', default=0, editable=False)
    result = models.BooleanField('Результат', default=False)

    def state(self):
        if self.all_record != 0:
            return (self.current_record*100) // self.all_record
        else:
            return 0

    def filename(self):
        return os.path.basename(self.file_path.name)


class FileResult(models.Model):
    source_addr = models.CharField('Исходный адрес', max_length=300)
    source_index = models.CharField('Исходный индекс', max_length=6, blank=True)
    get_addr = models.CharField('Полученный адрес', max_length=300)
    state = models.IntegerField('Статус', default=0)
    not_recognize = models.CharField('Полученный адрес', max_length=5, blank=True)
    accuracy = models.CharField('Код точности', max_length=3, blank=True)
    time_answer = models.IntegerField('Время ответа', default=0, blank=True)
    field_index = models.CharField('Индекс', max_length=6, blank=True)
    field_C = models.CharField('Страна', max_length=100, blank=True)
    field_R = models.CharField('Регион', max_length=100, blank=True)
    field_A = models.CharField('Район', max_length=100, blank=True)
    field_P = models.CharField('Населенный пункт', max_length=100, blank=True)
    field_T = models.CharField('Внутригородская территория', max_length=100, blank=True)
    field_S = models.CharField('Улично-дорожные элементы', max_length=100, blank=True)
    field_N = models.IntegerField('Номер дома', default=0, blank=True)
    field_NL = models.CharField('Литера', max_length=2, blank=True)
    field_D = models.CharField('Дробь', max_length=2, blank=True)
    field_E = models.IntegerField('Корпус', default=0, blank=True)
    field_B = models.IntegerField('Строение', default=0, blank=True)
    field_F = models.IntegerField('Помещение', default=0, blank=True)
    field_BOX = models.IntegerField('Абонентский ящик', default=0, blank=True)
    ident_low = models.CharField('Идентификатор нижнего уровня', max_length=50, blank=True)
    latitude = models.CharField('Широта',max_length=10, blank=True)
    longtitude = models.CharField('Долгота',max_length=10, blank=True)
    num_dest_post = models.IntegerField('Номер участка', default=0, blank=True)
    file_source = models.ForeignKey(FileParse, on_delete=models.CASCADE, blank=True)


class Billing(models.Model):
    date_req = models.DateField(auto_now=True)
    file = models.ForeignKey(FileParse, on_delete=models.Model)
    count_req = models.IntegerField(default=0)
