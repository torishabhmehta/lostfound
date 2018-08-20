from django.conf.urls import url, include
from rest_framework import routers
from .views import *

# Registering serializers on routers

router = routers.SimpleRouter()
router.register(r'lost', LostViewSet)
router.register(r'found', FoundViewSet)
urlpatterns = router.urls
