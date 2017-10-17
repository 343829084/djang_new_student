#-*-coding:utf-8-*-
from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    username = request.user.username
    print "webadmin.views.index, username=", username
    return render(request, 'index.html',{
            "title":u'主页',
            'username':username})

# Create your views here.
