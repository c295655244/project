 #coding=utf-8
from django.shortcuts import render_to_response
from mysite.contact.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail

def contact_thanks(request):
    return render_to_response('contact_thanks.html',context_instance=RequestContext(request))

def contact_form(request):
    return render_to_response('contact_form.html', context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})#subject字段将被那个句子填充
#在view里面，强制使用RequestContext 代替Context。示例如下
    return render_to_response('contact_form.html', {'form': form},context_instance=RequestContext(request))

