 #coding=utf-8
from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):#在这个列表中可以看到作者的邮箱地址。如果能按照姓氏或名字来排序，那就更好了
    list_display = ('first_name', 'last_name', 'email')#它是一个字段名称的元组，用于列表显示
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)#为日期型字段提供了快捷过滤方式，它包含：今天、过往七天、当月和今年
    date_hierarchy = 'publication_date'#页面中的列表顶端会有一个逐层深入的导航条，它从可用的年份开始，然后逐层细分到月乃至日。
    ordering = ('-publication_date',)#改变默认的排序方式，按publication date降序排列
    #fields = ('title', 'authors', 'publisher')#编辑表单将按照指定的顺序显示各字段,隐藏publication_date，以防止它被编辑
    filter_horizontal = ('authors',)#针对多对多字段
    raw_id_fields = ('publisher',)#包含外键字段名称的元组，它包含的字段将被展现成`` 文本框`` ，而不再是`` 下拉框``

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)#用AuthorAdmin选项注册Author模块
admin.site.register(Book, BookAdmin)