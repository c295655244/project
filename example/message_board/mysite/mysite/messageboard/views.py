# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import *
from django.views.generic.list import  ListView
from mysite.messageboard.models import Msg
from django.http import HttpResponse
# 导入在 forms.py 中定义的所有表单类。
from forms import *
# 导入 HttpResponseRedirect 类。
from django.http import HttpResponseRedirect
# 导入 RequestContext 类。
from django.template import RequestContext
# 导入 render_to_response 函数。
from django.shortcuts import render_to_response
# 请将以上这些导入语句放到 views.py 文件的开头。
# 定义 register_page 函数。
def register_page(request):
# 如果是通过 POST 方法提交注册表单数据而
# 调用该函数。
	if request.method == 'POST':
# 建立一个包含了用户注册信息的
#RegistrationForm 表单对象。
		form = RegistrationForm(request.POST)
# 如果用户提交的注册表单数据验证合法。
	if form.is_valid():
# 根据用户提交的注册信息在用户信息表中
# 建立一个新的用户对象。
		user = User.objects.create_user(
		username=form.clean_data['username'],
		password=form.clean_data['password1'],
		email=form.clean_data['email']
		)
# 跳转到注册成功的页面。
	return HttpResponseRedirect('/accounts/register/success/')
# 如果是直接调用该函数,则建立一个未绑定
# 任何数据的注册表单对象。
	else:
		form = RegistrationForm()
# 实例化一个 RequestContext 类的对象,
# (该对象包含当前登录用户对象,以及
# 在其第二个参数中以目录形式包含的一些
# 模板变量,这里是用单引号括起来的模板变
# 量 form ,其值为 form 变量的值),并将该对
# 象保存到 variables 变量中。
		variables = RequestContext(request, {'form': form})
# 把变量 variables 中的 RequestContext 对象
# 传递给 register.html 模板,并将该模板转换
# 为网页显示在浏览器中。
		return render_to_response ('registration/register.html',variables)