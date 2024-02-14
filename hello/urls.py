from django.urls import path
from hello import views
from django.conf import settings


urlpatterns = [
    path("",views.index,name='home'),
    path("set",views.setcookie),
    path("get",views.getcookie),
    path("del",views.delcookie),
    path("book_appointment",views.book_appointment),
]