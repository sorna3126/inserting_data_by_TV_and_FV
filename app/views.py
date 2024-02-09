from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse

# Create your views here.
class TemplateHtml(TemplateView):
    template_name='TemplateHtml.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Harsha'
        ECDO['age']=3
        return ECDO

class insertdatabyTV(TemplateView):
    template_name='insertdatabyTV.html'
    def get_context_data(self,**kwargs):
        ECFO=super().get_context_data(**kwargs)
        ECFO['CFO']=CollegeForm
        return ECFO

    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('Insert Data By Template View is done')

class insert_data_by_FV(FormView):
    template_name='insert_data_by_FV.html'
    form_class=CollegeForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Insert Data by Form View is done')


    

