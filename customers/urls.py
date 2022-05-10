from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'customers', views.CustomersViewSet,basename="customers")
# router.register(r'users', views.UserViewSet,basename="users")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]