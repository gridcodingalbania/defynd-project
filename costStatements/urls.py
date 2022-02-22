# shop/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('statistics/', views.statistics_view, name='litigation-statistics'),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/costs/<int:year>/', views.get_costs_chart, name='chart-costs'),
    path('table/cost-per-category/<int:year>/', views.cost_per_category_table, name='table-cost-per-category'),
    path('chart/cost-per-customer/<int:year>/', views.cost_per_customer_chart, name='chart-cost-per-customer'),
    path('chart/litigation-success/<int:year>/', views.litigation_success_chart, name='chart-litigation-success'),
    path('chart/litigation-registration-type/<int:year>/', views.litigation_registration_chart, name='chart-litigation-registration-type'),
]
