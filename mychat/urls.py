from django.contrib import admin
from django.urls import path, include
#импорты для настройки картинки
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mychat/', include('messenger.urls')),
    # path('', include('protect.urls')),
    # path('sign/', include('sign.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)