#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.list import  ListView
from mysite.messageboard  import models
from mysite import  messageboard
import os
# 得到 site_media 文件夹的实际位置,
# 并保存到 site_media1 中。
site_media1 = os.path.join(os.path.dirname(__file__),'templates/site_media')


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
    	model=models.Msg,
    	paginate_by=10,#留言对象列表的分页处理。
    	template_name= 'base.html',# 模板文件名称。
    	context_object_name= 'msg'# 对象列表的模板变量名称
    	)),#实现分页显示所有用户发 表 留 言 的 列 表
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root': site_media1}),
    # 显示注册成功的页面。
    url(r'^accounts/register/success/$','django.views.generic.simple.direct_to_template',{'template': 'registration/register_success.html'}),
    # 对 url 路径 /site_media/ 下的任何静态文件的访问
    # 都会由 serve 函数处理。
    url(r'^accounts/register/$', 'messageboard.views.register_page'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$','messageboard.views.logout',{'next_page': '/'}),
)
