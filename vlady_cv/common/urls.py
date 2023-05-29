from django.urls import path

from vlady_cv.common.views import Certificates, AddCertificate, Index, Knowledge, About

urlpatterns = (
    path('', Index.as_view(), name='index'),
    path('certificates/', Certificates.as_view(), name='certificates'),
    path('knowledge/', Knowledge.as_view(), name='knowledge'),
    path('about/', About.as_view(), name='about'),
    path('add/', AddCertificate.as_view(), name='add_certificate'),
)
