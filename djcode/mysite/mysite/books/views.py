 #coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from mysite.books.models import Book



def search_form(request):
    return render_to_response('search_form.html')

def search(request):#除了检查q是否存在于request.GET之外，我们还检查来reuqest.GET[‘q’]的值是否为空。
    errors = []
    if 'q' in request.GET:#当提交表单时，变量q的值通过GET(method=”get”)附加在URL /search/上
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})