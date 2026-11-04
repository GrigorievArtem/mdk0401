from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, GradeViewSet, AttendanceViewSet
router = DefaultRouter()
router.register("lessons", LessonViewSet)
router.register("grades", GradeViewSet)
router.register("attendance", AttendanceViewSet)
urlpatterns = router.urls
