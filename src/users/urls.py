from django.urls import path

from .forms import ManagerCreationForm, EmployerCreationForm
from .views import Login, Logout, Register

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register_manager/', Register.as_view(form_class=ManagerCreationForm), name='register_manager'),
    path('register_employer/', Register.as_view(form_class=EmployerCreationForm), name='register_employer'),
]
