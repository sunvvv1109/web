## 웹-프레임워크-djangopython-실습(windows10)

### 가상환경
- 가상환경 생성
```
(dj) D:\__sunchan\project\web> conda create -n dj python=3.7
```

- 가상환경 실행
```
D:\__sunchan\project\web>conda activate dj
```


### 프로젝트 생성

```
(dj) D:\__sunchan\project\web> django-admin startproject tutorial
(dj) D:\__sunchan\project\web> cd tutorial
```

### 앱 생성
```
(dj) D:\__sunchan\project\web\tutorial> python manage.py startapp community
```

- migrate
```
(dj) D:\__sunchan\project\web\tutorial> python manage.py migrate
```

- superuser 설정
```
(dj) D:\__sunchan\project\web> python manage.py createsuperuser
```


### 서버운영
- 서버 실행
```
(dj) D:\__sunchan\project\web> python manage.py runserver
```

- admin 페이지
브라우저(크롬)에 http://127.0.0.1:8000/admin/ 입력
Username: admin
Password: django0000


### 파일 수정
- d:\__sunchan\project\web\tutorial\community\models.py

```
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)
```


### 데이터베이스 생성 적용

```
(dj) D:\__sunchan\project\web> python manage.py makemigrations community
```

```
(dj) D:\__sunchan\project\web> python manage.py migrate
```

### 파일 수정
- (dj) d:\__sunchan\project\web\tutorial\tutorial\urls.py

```
from django.contrib import admin
from django.urls import path, include
from community.views import *

urlpatterns = [
    #path('bbs/write/', write, name='write'),
    # path('bbs/', lists, name='lists'),
    # path('bbs/view/3', view, name='view'),
    # path('bbs/edit/3', edit, name='edit'),
    path('bbs/write/', write, name='write'),
    path('admin/', admin.site.urls),
]
```


- (dj) d:\__sunchan\project\web\tutorial\community\views.py

```
from django.shortcuts import render

# Create your views here.
def write(request):
    return render(request, 'write.html')
```

## 파일 생성

- 폴더 생성: D:\__sunchan\project\web\tutorial\community\templates
- 파일 생성: D:\__sunchan\project\web\tutorial\community\templates\write.html


- write.html 편집
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>write</title>
  </head>
  <body>
hello django!!!!
  </body>
</html>
```

### form

```
from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields=['name', 'title', 'contents','url', 'email']
```

### list
- D:\__sunchan\project\web\tutorial\tutorial\urls.py 수정
- D:\__sunchan\project\web\tutorial\community\views.py 수정
- D:\__sunchan\project\web\tutorial\community\templates\list.html 생성

### view
- D:\__sunchan\project\web\tutorial\tutorial\urls.py 수정
- D:\__sunchan\project\web\tutorial\community\views.py 수정
- D:\__sunchan\project\web\tutorial\community\templates\view.html 생성

### write
- D:\__sunchan\project\web\tutorial\tutorial\urls.py 수정
- D:\__sunchan\project\web\tutorial\community\views.py 수정
- D:\__sunchan\project\web\tutorial\community\templates\write.html 생성

### edit
- D:\__sunchan\project\web\tutorial\tutorial\urls.py 수정
- D:\__sunchan\project\web\tutorial\community\views.py 수정
- D:\__sunchan\project\web\tutorial\community\templates\edit.html 생성