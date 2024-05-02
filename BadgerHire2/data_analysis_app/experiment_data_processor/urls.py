from django.urls import path
from .views import upload_csv, display_data

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('data/', display_data, name='display_data'),
]
