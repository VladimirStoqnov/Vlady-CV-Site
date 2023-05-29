from django.shortcuts import render
from django.views import generic as views

from vlady_cv.common.models import Certificate


class Index(views.ListView):
    queryset = []
    template_name = 'intro.html'


class Certificates(views.ListView):
    model = Certificate
    queryset = Certificate.objects.all()
    template_name = 'certificates.html'


class Knowledge(views.ListView):
    queryset = []
    template_name = 'knowledge.html'


class About(views.ListView):
    queryset = []
    template_name = 'about.html'


class AddCertificate(views.CreateView):
    template_name = 'add_certificate.html'
    model = Certificate
    fields = '__all__'

    success_url = '/certificates/'
