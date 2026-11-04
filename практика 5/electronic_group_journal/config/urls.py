from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("api/token/", obtain_auth_token, name="api_token"),
    path("api/clients/", include("apps.clients.urls")),
    path("api/catalog/", include("apps.catalog.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/reports/", include("apps.reports.urls")),
    path("", include("apps.reports.web_urls")),
]
