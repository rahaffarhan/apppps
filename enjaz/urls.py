from django.conf.urls import url, include
from django.contrib import admin
from events_attendance import views




urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^events_attendance/', include('events_attendance.urls')),
  # url(r'^accounts/', include('registration.backends.hmac.urls')),

]


#urlpatterns += staticfiles_urlpatterns()