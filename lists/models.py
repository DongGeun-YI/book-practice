from django.db import models
# Create your models here.


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    #List객체를 문자열로 해석해서 저장하고있으므로, 객체자체를 저장하기 위해 For-를 사용


