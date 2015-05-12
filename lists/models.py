from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class List(models.Model):
    def get_absoloute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    #List객체를 문자열로 해석해서 저장하고있으므로, 객체자체를 저장하기 위해 For-를 사용



