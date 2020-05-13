from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import api_root
from snippets.urls import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

urlpatterns += [
    path('test-auth/', include('rest_framework.urls')),
]