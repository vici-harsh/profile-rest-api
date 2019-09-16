from django.urls import path,include
from rest_framework.routers import DefaultRouter # for viewset
from profiles_api import views

# way to specify the url for viewset
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name="hello-ViewSet")
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
