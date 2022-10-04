from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import PartnerUpdate, PartnerState, RegisterAccount, ConfirmAccount, AccountDetails, ContactView, \
    LoginAccount, CategoryView, ShopView, BasketView, OrderView, ProductInfoViewSet

app_name = 'backend'

product_info = ProductInfoViewSet.as_view({
    'get': 'product_info'
})


router = DefaultRouter()
# router.register('partner/update', PartnerUpdate.as_view())
router.register('products', ProductInfoViewSet, basename='product_info')



urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('categories', CategoryView.as_view(), name='categories'), # Нужно доработать
    path('shop', ShopView.as_view(), name='shop'),
    # path('products', ProductInfoView.as_view(), name='products'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('products', include(router.urls)),
]