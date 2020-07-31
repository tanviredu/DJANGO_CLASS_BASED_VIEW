from django.urls import path
from . import views
app_name = "CLSBV"

urlpatterns = [
    path('',views.index,name="index"),
    path('class',views.indexView.as_view(),name='index_class'),
    path('index',views.ViewTemplate.as_view(),name='view_template'),
    path('list',views.ShowList.as_view(),name='view_list'),
    path('album_list',views.ShowAlbumList.as_view(),name='view_album'),
    path('musician_detail/<int:pk>',views.MusicianDetail.as_view(),name='mdetail'),
    path('album_detail/<int:pk>',views.AlbumDetail.as_view(),name='adetail'),
    path('addmusician',views.CreateMusician.as_view(),name='addm'),
    path('addAlbum',views.CraeteAlbum.as_view(),name='addal'),
    path('updatem/<int:pk>',views.UpdateMusician.as_view(),name='updatem'),
    path('updatea/<int:pk>',views.UpdateAlbum.as_view(),name='updatea'),
    path('deletea/<int:pk>',views.DeleteAlbum.as_view(),name='deletea'),
    path('deletem/<int:pk>',views.DeleteMusician.as_view(),name='deletem'),



]