from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import Static_Sitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': Static_Sitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name='password_reset_complete'), 
     path('sitemap.xml', sitemap, {'sitemaps': sitemaps,'template_name': 'custom_sitemap.html'}, name='django.contrib.sitemaps.views.sitemap'),
     path('', include('social_django.urls', namespace='social')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]
