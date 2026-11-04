from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .services import get_journal_stats, group_performance

@login_required
def dashboard(request):
    return render(request, "dashboard.html",
                  {"stats": get_journal_stats(), "groups": group_performance()})

urlpatterns = [path("", dashboard, name="dashboard")]
