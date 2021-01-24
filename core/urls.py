from django.urls import path
from .views import index, produto

from django.conf.urls import handler404, handler500
from core import views


urlpatterns= [
    path('', index, name='index'),
    path ('produto/<int:pk>', produto, name = 'produto'),
]

handler404 = views.error404
handler500 = views.error500
