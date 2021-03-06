from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.users.urls', namespace='users')),
    path('', include('src.parking.urls', namespace='parking')),
    # path('', TemplateView.as_view(template_name='base.html'), name='home'),
]
