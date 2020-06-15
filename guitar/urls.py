from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf.urls.static import static
from django.conf import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses, name='courses'),
    #including courses URL path
    path('main/', include('main.urls')),

    path('', TemplateView.as_view(template_name="social_app/index.html")),
    
    path('register/',user_views.register, name='register'),
    path('sent/', user_views.activation_sent_view, name='activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/', user_views.activate, name ='activate'),

    path('profile/',user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
    name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
    name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
    name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
    name='password_reset_complete'),

    #social
    path('social-auth/', include('social_django.urls', namespace="social")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
