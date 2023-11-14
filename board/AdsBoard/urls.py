from django.urls import path

from .models import Ads
from .views import IndexView, AdvertisementCreate, AdvertisementView, advertisement_detail


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', AdvertisementCreate.as_view(), name='create'),
    path('take/', AdvertisementView.as_view(queryset=Ads.objects.filter(category__id=1)), name='post_list'),
    path('give/', AdvertisementView.as_view(queryset=Ads.objects.filter(category__id=2)), name='post_list'),
    path('services/', AdvertisementView.as_view(queryset=Ads.objects.filter(category__id=3)), name='post_list'),
    path('take/<int:post_id>', advertisement_detail, name='post'),
    path('give/<int:post_id>', advertisement_detail, name='post'),
    path('services/<int:post_id>', advertisement_detail, name='post'),
]