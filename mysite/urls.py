"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from blog import views -> blog/urls.py에서 다시 import

# mysite는 프로젝트의 내용이므로 여기엔 프로젝트 관련 url 매핑만 추가되어야 함.
# 따라서 다음과 같이 include를 사용해 blog의 url로 따로 분류.
urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls')),
]
