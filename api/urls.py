from django.urls import path
# from .views import LatLongAPIView
from api import views as api_views

urlpatterns = [
    # path('', LatLongAPIView.as_view()),
    path('', api_views.latlong_list),
]
