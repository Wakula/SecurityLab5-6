from django.urls import include
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('storage/', include('storage.urls')),
    path('', RedirectView.as_view(url='storage/login', permanent=True)),
]
