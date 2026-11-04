from django.urls import path
from .views import JournalStatsAPIView
urlpatterns = [path("stats/", JournalStatsAPIView.as_view(), name="journal-stats")]
