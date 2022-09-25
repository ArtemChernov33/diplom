from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PartnerUpdate, PartnerState, RegisterAccount, ConfirmAccount, AccountDetails, ContactView

# router = DefaultRouter()
# router.register('partner/update', PartnerUpdate.as_view())


app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),

]