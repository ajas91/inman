from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'items', views.ItemViewSet,basename="items")
router.register(r'items_category', views.ItemCategoryViewSet,basename="items_category")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
]