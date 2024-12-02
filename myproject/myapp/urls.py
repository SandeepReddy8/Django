from django.urls import path
from .views import ItemCreateAPIView

urlpatterns = [
    path('items/create/', ItemCreateAPIView.as_view(), name='item-create'),
]
