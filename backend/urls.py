from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PartnerUpdate, PartnerState

# router = DefaultRouter()
# router.register('partner/update', PartnerUpdate.as_view())


app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),


]