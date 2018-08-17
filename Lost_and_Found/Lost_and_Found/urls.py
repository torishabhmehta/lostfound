from django.contrib import admin
from django.urls import path, include
from LostFound import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('LostFound.urls'))
]
