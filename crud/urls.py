from rest_framework import routers
from .views import StudentViewSet, ClassLevelViewSet, SchoolViewSet, TeacherViewSet
from django.urls import path, include

app_name = "crud_api"
router = routers.SimpleRouter()
router.register(r"students", StudentViewSet)
router.register(r"class-level", ClassLevelViewSet)
router.register(r"school", SchoolViewSet)
router.register(r"teacher", TeacherViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
