from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import StMaroc
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
import csv,io
# Create your views here.
class GlobalChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/chart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class DeathChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/deathstat.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class QuoChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/quotidien_cas.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class QuoDeathChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/quotidien_morts.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class CumulTestChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/testC.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class QuoTestChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/quotest.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class QuoRecChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/quorec.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context

class TabChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/tabSt.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context



#@permission_required('admin.can_add_log_entry')
class DetailsChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/baseStM.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context


class CUMChart(TemplateView):
    """docstring for ."""
    template_name='STMaroc/recovSt.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["qs"]=StMaroc.objects.all()
        return context


@permission_required('admin.can_add_log_entry')
def contact_uploadSt(request):
    template='uploadStMaroc.html'
    contexte={
        'order' : 'Order should be ,Date,Tot cases,New cases,Tot Deaths,New Deaths,Total Recovered,Active Cases,Serious,Tot C par million,Deaths par million,Total Test,Tot T par million,Country,Continent,index,population'
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
        _, created=StMaroc.objects.update_or_create(
        date=column[1],
        cases=column[2],
        casesD=column[3],
        death=column[4],
        deathD=column[5],
        recov=column[6],
        recovD=column[-4],
        tests=column[11],
        )
    context={}
    return render(request,template, context)
