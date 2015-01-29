# -*- coding: utf-8 -*-
from django.db import models# 导入用户信息表对应的用户数据模型。
from django.contrib.auth.models import User# 定义留言信息表数据模型 Msg ,

class Msg(models.Model):
    title = models.CharField(max_length=30)# 用于存取留言标题。
    content = models.TextField()# 并将其保存到 content 属性中,
    user = models.ForeignKey(User)# 该字段引用用户信息表 id 字段的值,是用户, 信息表的外键,用于存取留言用户的 id 信息。
    ip = models.IPAddressField()# 用于存取留言者计算机的 ip 地址信息。
    datetime = models.DateTimeField(auto_now_add=True)# 自动设置该属性值为当前时间。
    clickcount = models.IntegerField(default=0)# 用于存取留言的点击次数信息。

def __str__(self):# 定义该数据模型对象的字符串表示,其功能
    return' 用户 %s 发表的标题为 %s 的留言' % (self.user.username, self.title)
