from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns






urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^events_attendance/', include('events_attendance.urls')),

]


urlpatterns += staticfiles_urlpatterns()