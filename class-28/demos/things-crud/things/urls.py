from django.urls import path
from .views import ThingListView, ThingCreateView, ThingDetailView, ThingDeleteView, ThingUpdateView

urlpatterns = [
    path('', ThingListView.as_view(), name='thing_list'),
    path('<int:pk>/', ThingDetailView.as_view(), name='thing_detail'),
    path('<int:pk>/update/', ThingUpdateView.as_view(), name='thing_update'),
    path('create/', ThingCreateView.as_view(), name='thing_create'),
    path('<int:pk>/delete/', ThingDeleteView.as_view(), name='thing_delete'),
]
