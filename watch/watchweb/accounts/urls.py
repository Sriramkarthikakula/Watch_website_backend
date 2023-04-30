from django.urls import path
from . import views

urlpatterns = [
    path('logins',views.logins,name='logins'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name="logout"),
    path('adminlog',views.adminlog,name="adminlog"),
    path('admin',views.admin,name="admin"),
    path('intercall1',views.intercall1,name="intercall1"),
    path('inter',views.inter,name="inter"),
]