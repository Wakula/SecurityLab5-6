from django.urls import include
from django.urls import path

urlpatterns = [
    path('storage/', include('storage.urls')),
]
