from django.urls import path
from .views import GetInfoView

urlpatterns = [
    path('info/', GetInfoView.as_view(), name='get_info'),
]
