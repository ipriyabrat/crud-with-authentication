 
 
from django.urls import path,include
from testapp.api.views import BookView
from rest_framework import routers
router=routers.DefaultRouter()
router.register('',BookView)

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token

urlpatterns = [
     path('',include(router.urls)),
     path('api-token-auth/',obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    
]