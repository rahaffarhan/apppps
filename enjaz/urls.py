from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from events_attendance import views as app_view
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

   url(r'^admin/', admin.site.urls),
   url(r'^', include('events_attendance.urls')),
   url(r'^register/$', user_views.register, name='register'),
   url(r'^profile/$', user_views.profile, name='profile'),
   url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
   url(r'^logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)