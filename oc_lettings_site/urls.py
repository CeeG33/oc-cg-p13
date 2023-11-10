from django.contrib import admin
from django.urls import include, path

from . import views


def _trigger_error(request):
    return 1 / 0


handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', _trigger_error),
    path('404/', views.custom_404, name='custom_404'),
    path('500/', views.custom_500, name='custom_500')
]
