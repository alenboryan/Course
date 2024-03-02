from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', include('polls.urls')), # Include the polls app's URLs for the empty path
    path('admin/', admin.site.urls),
]