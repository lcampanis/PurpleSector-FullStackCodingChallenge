from rest_framework import routers
from codingchallenge import views, apps

app_name = apps.CodingchallengeConfig.name

router = routers.DefaultRouter()
router.register(r"race-data", views.EventRaceDataViewSet, basename="race-data")
urlpatterns = router.urls
