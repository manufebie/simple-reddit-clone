from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
