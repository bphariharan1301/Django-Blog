from os import stat
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('myblog.urls') ),
    path('members/', include('django.contrib.auth.urls') ),
    path('members/', include('members.urls') ),
    # path('members/', include('members.urls') ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
