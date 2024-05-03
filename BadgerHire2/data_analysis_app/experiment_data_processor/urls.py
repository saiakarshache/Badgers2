# from django.urls import path
# from .views import upload_csv, display_data

# urlpatterns = [
#     path('upload/', upload_csv, name='upload_csv'),
#     path('data/', display_data, name='display_data'),
# ]

# from django.urls import path
# from . import views  # Import the views module from the current package

# urlpatterns = [
#     path('upload/', views.upload_csv, name='upload_csv'),  # Use the views.upload_csv function
#     path('data/', views.display_data, name='display_data'),
# ]

from django.urls import path
from . import views  # Import the views module from the current package

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),  # Use the views.upload_csv function
    path('data/', views.display_data, name='display_data'),
    path('get_data/', views.get_data, name='get_data'),  # Add URL mapping for get_data view
]

