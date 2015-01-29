# -*- coding: utf-8 -*-
# 导入 newforms 包,并重命名为 forms 。
from django import newforms as forms
# 导入正则表达式模块。
import re
# 导入用户数据模型。
from django.contrib.auth.models import User
# 导入 ObjectDoesNotExist 类。
from django.core.exceptions import ObjectDoesNotExist
# 定义用户注册表单类 RegistrationForm ,
# 该类从 Form 类继承。
class RegistrationForm(forms.Form):
# 实例化一个用于输入用户名的文本框对象,
# 并将该对象保存到 username 属性中。
	username = forms.CharField(label=' 用 户 名 ', max_length=30)
# 实例化一个用于输入用户电子邮件地址的
# 文本框对象,并将该对象保存到 email 属性中。
	email = forms.EmailField(label=' 电子邮件 ')
# 实例化一个用于输入用户密码的文本框对象,
# 并将该对象保存到 password1 属性中。
	password1 = forms.CharField(label=' 密码 ',widget=forms.PasswordInput())
# 实例化一个用于输入用户确认密码的文本框对象,
# 并将该对象保存到 password2 属性中。
	password2 = forms.CharField(label=' 确认密码 ',
	widget=forms.PasswordInput()
	)
# 该函数用于验证用户输入用户名的合法性。
def clean_username(self):
# 从通过一般性验证的用户名输入文本框中
# 取出用户输入的用户名,并保存到
# 变量 usename 中。
	username = self.clean_data['username']
# 借助正则表达式检查用户名是否由字母、
# 数字和下划线组成。
	if not re.search(r'^\w+$', username):
		raise forms.ValidationError (' 用户名中只能包含字母、数字和下划线! ')
	try:
# 从用户数据模型中取出 username 属性
# 等于 username 变量值的用户对象。
# 如果在用户数据模型中不存在该用户对象,
# 则引发一个异常。
		User.objects.get(username=username)
# 异常处理。
	except ObjectDoesNotExist:# 返回 username 变量的值。
		return username
# 如果在用户数据模型中存在该用户对象,
# 则引发一个 ValidationError 异常。
	raise forms.ValidationError(' 用户名已存在! ')
# 该函数用于验证用户输入电子邮件地址的合法性。
def clean_email(self):
# 从通过一般性验证的电子邮件地址输入文本框中
# 取出用户输入的电子邮件地址,并保存到
# 变量 email 中。
	email = self.clean_data['email']
	try:
# 从用户数据模型中取出 email 属性
# 等于 email 变量值的用户对象。
# 如果在用户数据模型中不存在该用户对象,
# 则引发一个异常。
		User.objects.get(email=email)
# 异常处理。
	except ObjectDoesNotExist:
# 返回 email 变量的值。
		return email
# 如果在用户数据模型中存在该用户对象,
# 则引发一个 ValidationError 异常。
	raise forms.ValidationError (' 用户数据 库 中 已 有 该 电 子 邮 件! ')
# 该函数用于验证用户两次输入密码一致性。
def clean_password2(self):
	if 'password1' in self.clean_data:
# 从通过一般性验证的用户密码输入文本框中
# 取出用户输入的密码,并保存到变量
#password1 中。
		password1 = self.clean_data['password1']
# 从通过一般性验证的用户确认密码输入文本
# 框中取出用户输入的确认密码,并保存到
# 变量 password2 中。
		password2 = self.clean_data['password2']
	if password1 == password2:
		return password2
# 如果用户两次输入的新密码不一致,则
# 引发一个 ValidationError 异常。
	raise forms.ValidationError(' 密码不匹配 ')