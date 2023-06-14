from django.urls import path, include

from vlady_cv.common.views import Certificates, AddCertificate, Index, Knowledge, About, DetailsCertificate

urlpatterns = (
    path('', Index.as_view(), name='index'),
    path('certificates/', include([
        path('', Certificates.as_view(), name='certificates'),
        path('details/<int:pk>', DetailsCertificate.as_view(), name='details')
    ])),
    path('knowledge/', Knowledge.as_view(), name='knowledge'),
    path('about/', About.as_view(), name='about'),
    path('add/', AddCertificate.as_view(), name='add_certificate'),
)
