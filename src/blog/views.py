from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render
from django.http.response import JsonResponse
import json

# Create your views here.
def archive(request):
    '''posts=BlogPost.objects.all()
    print('posts:%s'%posts[0].title)
    t=loader.get_template('archive.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))'''
    posts=json.dump(BlogPost.objects.all())
    context={}
    context['posts']=posts
    return render(request,'archive.html',context)