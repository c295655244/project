 #coding=utf-8
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __unicode__(self):
        return self.name
        class Meta:
            ordering = ['name']               

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True,verbose_name='e-mail')#自定义字段标签
    #email = models.EmailField('e-mail',  blank=True)但这不适用于ManyToManyField 和ForeignKey字段，因为它们第一个参数必须是模块类。 那种情形，必须显式使用verbose_name这个参数名称。
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.title
# Create your models here.