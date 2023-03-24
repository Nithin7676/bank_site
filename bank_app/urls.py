from django.urls import path
from .import views
urlpatterns = [
    path('', views.index),
    path('login_page/', views.login_page),
    path('registration_page/', views.registration_page),
    path('save_registration/', views.save_registration),
    path('user_home/', views.user_home),
    path('user_login_check/', views.user_login_check),
    path('application_form/', views.application_form),
    path('sub_area_view/',views.sub_area_view),
    path('save_application/', views.save_application),
    path('success_page/', views.success_page),
]