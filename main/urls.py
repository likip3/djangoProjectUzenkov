from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('demand', views.demand, name='demand'),
    path('geo', views.geo, name='geo'),
    path('skills', views.skills, name='skills'),
    path('recent', views.recent, name='recent'),
]
