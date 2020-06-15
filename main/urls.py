from . import views
from django.urls import path, include
from .views import VideoListView
urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('material/<str:cat>/',VideoListView.as_view(), name="videoListView"),
    path('material/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('contact/', views.contact, name='contact'),
]
