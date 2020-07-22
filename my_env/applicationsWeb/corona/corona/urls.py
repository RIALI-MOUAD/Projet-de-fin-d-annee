"""corona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , include
from countries.views import * #GlobalChartView, DeathChartView,RecoverChartView,contact_upload,NewCasesChartView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import *
from StMaroc.views import *
from django.conf import settings
from django.conf.urls.static import static
from predict.views import *

app_name='blog'
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', home, name='home'),
    path('global',GlobalChartView.as_view() , name='global' ),
    path('death' ,DeathChartView.as_view() , name='death'),
    path('recover' , RecoverChartView.as_view(), name='recover'),
    path('upload', contact_upload , name='contact_upload'),
    path('uploadStMaroc', contact_uploadSt , name='contact_uploadSt'),
    path('new-cases', NewCasesChartView.as_view(), name='newc'),
    path('base-csv', DetailsChartView.as_view(), name ='details'),
    path('base-csv-st-maroc', DetailsChart.as_view(),name='BaseStMaroc'),
    path('tab-data' ,TableauChartView.as_view(), name= 'tableau'),
    path('stat-mar', GlobalChart.as_view(), name='stat'),
    path('death-stat-mar', DeathChart.as_view(), name='deathstat'),
    path('cas-par-jour',QuoChart.as_view() , name='quotidien'),
    path('Cumul-des-tests-par-jour',CumulTestChart.as_view(),name='testC'),
    path('Death-par-jour', QuoDeathChart.as_view(), name='quomort'),
    path('test-par-jour', QuoTestChart.as_view() , name='quotest'),
    path('recover-par-jour',QuoRecChart.as_view() , name='quorecov'),
    path('commul-recover-maroc',CUMChart.as_view(), name='cumrecov'),
    path('tab-stat-Maroc-par-date', TabChart.as_view(),name='tabSt'),
    path('blog' , include('blog.urls' , namespace='blog')),#    path('blog-post-covid-19-st', all_post ,name='blog')
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
