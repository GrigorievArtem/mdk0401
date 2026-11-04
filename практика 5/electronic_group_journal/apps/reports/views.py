from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_journal_stats, group_performance

class JournalStatsAPIView(APIView):
    def get(self, request):
        return Response({"summary": get_journal_stats(),
                         "groups": group_performance()})
