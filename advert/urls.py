from django.urls import path
from advert.views import AdvertListAPIView, AdvertDetailAPIView

urlpatterns = [
    path('advert-list/', AdvertListAPIView.as_view(), name='advert-list'),
    path('advert/<int:id_advert>/', AdvertDetailAPIView.as_view(), name='advert-detail'),
]