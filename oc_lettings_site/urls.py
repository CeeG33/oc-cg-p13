from django.contrib import admin
from django.urls import include, path

from . import views


def _trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', _trigger_error)
]
