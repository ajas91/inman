from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'orders', views.OrdersViewSet,basename="orders")
router.register(r'orderline', views.OrderLineViewSet,basename="orderline")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]