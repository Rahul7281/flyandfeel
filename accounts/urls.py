from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('accounts/register', views.register, name='register'),
    # path('accounts/login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='about'),
    path('news.html', views.news, name='news'),
    path('destinations.html', views.destinations, name='destinations'),
    path('package.html', views.package, name='package'),
    path('service.html', views.service, name='service'),
    path('International_packages.html', views.International_packages, name='International_packages'),
    path('Domestic_packges.html', views.Domestic_packges, name='Domestic_packges'),
    # path('accounts/package_details.html', views.package_details, name='package_details'),
    path('<int:id>/package_details.html', views.package_details, name='package_details'),

    #  path('package-details/<int:id>/', views.package_details, name='package_details'),
    path('signup.html', views.signup, name='signup'),
    path('signin.html', views.signin, name='signin'),
    path('my_booking.html', views.my_booking, name='my_booking'),
    path('admin_homepage.html', views.admin_homepage, name='admin_homepage'),
    path('team.html', views.team, name='team')
    # path('clear-login-success-flag/', views.clear_login_success_flag, name='clear_login_success_flag'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)