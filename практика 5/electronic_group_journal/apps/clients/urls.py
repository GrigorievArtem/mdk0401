from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet, StudentViewSet
router = DefaultRouter()
router.register("study-groups", StudyGroupViewSet)
router.register("students", StudentViewSet)
urlpatterns = router.urls
