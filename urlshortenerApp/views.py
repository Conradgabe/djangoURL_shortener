from django.shortcuts import render, redirect
import uuid

from .models import LinkURL

import datetime

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        links = request.POST['original']
        link = LinkURL(original_url=links)
        link.save()
        # return redirect('redirect')
    else:
        return redirect('index')
    today = datetime.date.today()
    url = LinkURL.objects.filter(date_created__gte=today)
    context = {
        'links':links,
        'obj': url[len(url)-1]
    }
    return render(request, 'index.html', context)

def redirect_url(request, url):
    current_obj = LinkURL.objects.filter(shorten_url=url)
    return render(request, 'index.html', {
        'obj': current_obj
    })