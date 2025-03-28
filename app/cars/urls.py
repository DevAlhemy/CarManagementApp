from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
