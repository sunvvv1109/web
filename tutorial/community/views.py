from django.shortcuts import redirect
from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        form =Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/bbs/')
    else:
        form =Form()

    return render(request, 'write.html', {'form':form})
    
def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})

def edit(request, num="1"):
    article = Article.objects.get(id=num)
    if request.method == 'POST':
        article.name = request.POST['name']
        article.title = request.POST['title']
        article.contents = request.POST['contents']
        article.url = request.POST['url']
        article.email = request.POST['email']
        article.save()
        return redirect(f'/bbs/view/{ num }')
    return render(request, 'edit.html', {'article':article})

# def edit_feed(request, dj):
#     article = Article.object.get(dj=dj)
#     return render(request, 'edit_feed.html',{'feed': article})