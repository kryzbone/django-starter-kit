from rest_framework.routers import SimpleRouter

from .views import CustomRegistrationViewSet, UserViewSet

router = SimpleRouter()
djoser_router = SimpleRouter()
router.register("", UserViewSet)
djoser_router.register("users", CustomRegistrationViewSet)

urlpatterns = router.urls
