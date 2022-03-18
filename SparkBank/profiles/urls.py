from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "profiles"

urlpatterns = [
    url(r"^account_status/$", views.index, name = "account_status"),
    url(r"^money_transfer/", views.money_transfer, name = "money_transfer"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
