from django.contrib import admin
from django.urls import include, path

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin area'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls', namespace='e-store')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('__debug__/', include('debug_toolbar.urls'))
]