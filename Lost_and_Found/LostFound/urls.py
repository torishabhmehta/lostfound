from django.conf.urls import url, include
from rest_framework import routers
from .views import *




router = routers.SimpleRouter()
router.register(r'lost', LostViewSet)
router.register(r'found', FoundViewSet)
router.register(r'spam', SpamViewSet, base_name='spam')
urlpatterns = router.urls
