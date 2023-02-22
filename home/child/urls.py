from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('eadmin', views.eadmin, name='eadmin'),
    path('eadmin/update/<int:pk>', views.updateView, name='update'),
    path('eadmin/delete/<int:pk>', views.deleteView, name='delete'),
    path('login', views.LoginView, name='login' ),
    path('logout', views.LogoutView, name='logout')
]