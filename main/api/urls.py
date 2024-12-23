from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()


router.register('chairman',views.ChairmanViewSet, basename='chairman' )
router.register('MFY', views.MFYViewSet, basename='MFY')
router.register('neighborhood', views.NeighborhoodViewSet, basename='neighborhood')
router.register('house', views.HouseViewSet, basename='house')
router.register('human', views.HumanViewSet, basename='human')




urlpatterns = router.urls