from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134137ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134137", Testconnectors134137ViewSet, basename="testconnectors134137"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
