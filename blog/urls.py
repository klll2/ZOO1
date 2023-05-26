from django.urls import path
from . import views

# mysite/urls.py의 blog/와 ''가 합쳐져  최종 url은 blog/가 됨.
urlpatterns = [
    path('', views.zindex, name = 'zindex'),

]