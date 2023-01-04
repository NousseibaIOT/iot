from . import views
from app import api
from django.urls import path
urlpatterns = [
 path('', views.dht11, name='data'),
 path('data2/', views.dht112, name='data2'),
 path('data3/', views.dht113, name='data3'),
 path('jr1/', views.data24, name='jr1'),
 path('jr1Graphe/', views.data24Graphe, name='jr1Graphe'),
 path('jr2/', views.data48, name='jr2'),
 path('jr2Graphe/', views.data48Graphe, name='jr2Graphe'),
 path('jr3/', views.data72, name='jr3'),
 path('jr3Graphe/', views.data72Graphe, name='jr3Graphe'),
 path('historique/', views.historique, name='historique'),



##api
 path('api/list', api.Dlist, name='DHT11list'),
# genericViews
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]

