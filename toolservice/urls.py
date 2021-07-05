from django.conf.urls import url, include
import toolservice.views as views

urlpatterns = [
    url('testPost/', views.testPost, name='testPost'),
    url('use_rouge/', views.use_rouge, name='use_rouge')
]