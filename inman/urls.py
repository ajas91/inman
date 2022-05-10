from django.contrib import admin
from django.urls import include,path,re_path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^', include('customers.urls')),
    re_path('^', include('inventory.urls')),
    re_path('^', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]