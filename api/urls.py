from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token, verify_jwt_token,)
from .views import (
    #DatosPostalesViewSet,
    MensajeroViewSet,
    ClienteViewSet,
    OrdenViewSet,
)

router = SimpleRouter()
#router.register(r'datos', DatosPostalesViewSet)
router.register(r'mensajeros', MensajeroViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ordenes', OrdenViewSet)
urlpatterns = [
    url(r'^auth/$', obtain_jwt_token),
    url(r'^refresh/$', refresh_jwt_token),
    url(r'^verify/$', verify_jwt_token),

]
urlpatterns += router.urls