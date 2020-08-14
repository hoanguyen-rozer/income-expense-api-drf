from django.urls import path
from .views import IncomeListAPIView, IncomeDetailAPIView


urlpatterns = [
    path('', IncomeListAPIView.as_view(), name='list-income'),
    path('<int:id>', IncomeDetailAPIView.as_view(), name='detail-income'),
]