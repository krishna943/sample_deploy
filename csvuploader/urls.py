from django.urls import path
from . import views
from .views import homes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homes, name='homes'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)