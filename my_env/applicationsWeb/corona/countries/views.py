from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Country
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import csv,io
# Create your views here.
def home(request):
    context={
     'home':home
    }
    return render(request,'corona/home.html',context)
class GlobalChartView(TemplateView):
    """docstring for ."""
    template_name='corona/chart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context


class DeathChartView(TemplateView):
    """docstring for ."""
    template_name='corona/death.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context


class RecoverChartView(TemplateView):
    """docstring for ."""
    template_name='corona/recov.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context

class NewCasesChartView(TemplateView):
    """docstring for ."""
    template_name='corona/newC.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context

class DetailsChartView(TemplateView):
    """docstring for ."""
    template_name='corona/details.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context

class TableauChartView(TemplateView):
    """docstring for ."""
    template_name='corona/tab.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context

class TestsChartView(TemplateView):
    """docstring for ."""
    template_name='corona/tests.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=Country.objects.all()
        return context


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template='upload.html'
    contexte={
        'order' : 'Order should be Country,Total cases,New cases,Total Death, New Death,Total R,Active C,Serious,Tot cases par mill,death per mill,Total Tests'
    }
    if request.method == "GET":
        return render(request, template, contexte)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'fichier non valide')

    data_set=csv_file.read().decode('UTF-8')
    io_String= io.StringIO(data_set)
    next(io_String)
    for column in csv.reader(io_String, delimiter=',', quotechar='|'):
        _, created=Country.objects.update_or_create(
            name=column[1],
            cases=column[2],
            New_cases=column[3],
            death=column[4],
            New_Deaths=column[5],
            Recover=column[6],
            Active_Cases=column[7],
            Serious=column[8],
            cases_million=column[9],
            deaths_million=column[10],
            tests=column[11],
            test_million=column[12],
            continent=column[13],
        )
    context={}
    return render(request,template, context)
