from django.shortcuts import render, get_object_or_404
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


class DetailsCertificate(views.DetailView):
    model = Certificate
    queryset = Certificate.objects.all()
    template_name = 'certificate_details.html'

    def get_object(self, queryset=None):
        pk = self.kwargs['pk']
        return self.model.objects.get(pk=pk)


class AddCertificate(views.CreateView):
    template_name = 'add_certificate.html'
    model = Certificate
    fields = '__all__'

    success_url = '/certificates/'
