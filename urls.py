from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی
    path('fields/', views.field_list, name='field_list'),
    path('fields/<int:field_id>/crops/', views.crop_list, name='crop_list'),
    path('fields/<int:field_id>/activities/', views.activity_list, name='activity_list'),
    path('add-field/', views.add_field, name='add_field'),
    path('add-crop/', views.add_crop, name='add_crop'),
    path('add-activity/', views.add_activity, name='add_activity'),
]