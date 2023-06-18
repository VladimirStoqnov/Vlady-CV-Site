from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views import generic as views
from vlady_cv.common.models import Certificate


class Index(views.ListView):
    queryset = []
    template_name = 'intro.html'


class Login(LoginView):

    template_name = 'login.html'


class Logout(LogoutView):
    template_name = 'logout.html'


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


class AddCertificate(UserPassesTestMixin, views.CreateView):
    template_name = 'add_certificate.html'
    model = Certificate
    fields = '__all__'

    success_url = '/certificates/'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('index')  # Replace 'index' with your index URL name or path

