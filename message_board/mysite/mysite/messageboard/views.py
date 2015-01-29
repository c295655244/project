 #coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from mysite.messageboard.models import *
from django.forms import *
from django.contrib.auth.decorators import login_required
from mysite.messageboard.forms import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

@login_required#使用这个方法是要求用户登录的
def msg_post_page(request):#用户发表留言
    if request.method=='POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = MsgPost(title=form.cleaned_data['title'],
                             content=form.cleaned_data['content'],
                             user=request.user
                             )
            newmessage.save()
        return HttpResponseRedirect('/mains/')
    else:
        form=MsgPostForm()
    variables=RequestContext(request,{'form':form})
    return render_to_response('msg_post_page.html',variables)



items_per_page=10

def mains(request):#显示主页
    #posts = MsgPost.objects.all()#get all records
    #return render_to_response('main.html',{'posts':posts})
    contact_list = MsgPost.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('main.html',{'posts':contacts,'request':request})




def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user( username=form.cleaned_data['username'],
                                             email=form.cleaned_data['email'],
                                             password=form.cleaned_data['password1'])
            return HttpResponseRedirect('/main/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request,{'form':form})
    return render_to_response('registration/register.html',variables)