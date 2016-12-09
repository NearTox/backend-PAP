from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token, verify_jwt_token)
from .views import DatosPostalesViewSet

router = SimpleRouter()
router.register(r'datos', DatosPostalesViewSet)
urlpatterns = [
    url(r'^auth/$', obtain_jwt_token),
    url(r'^refresh/$', refresh_jwt_token),
    url(r'^verify/$', verify_jwt_token),

]
urlpatterns += router.urls