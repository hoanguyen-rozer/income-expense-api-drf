from .views import ExpenseSummaryStatsAPI, IncomeSourceSummaryStatsAPI
from django.urls import path

urlpatterns = [
    path('expense-category-data/', ExpenseSummaryStatsAPI.as_view(),
         name='expense-category-summary'),
    path('income-source-data/', IncomeSourceSummaryStatsAPI.as_view(),
         name='income-source-summary'),

]
