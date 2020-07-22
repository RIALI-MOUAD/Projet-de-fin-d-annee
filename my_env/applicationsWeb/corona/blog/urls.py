from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name= 'blog'
urlpatterns= [
     url(r'^$' , views.all_posts, name='all_posts'),
     url(r'^/(?P<id>\d+)$', views.post , name='post')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
