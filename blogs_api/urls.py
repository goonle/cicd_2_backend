from django.urls import path
from .views import BlogLikeAPIView, BlogListCreateView, BlogRetrieveUpdateDestroyView, LoginAPIView, LogoutAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path("blogs/<int:pk>/", BlogRetrieveUpdateDestroyView.as_view(), name="blog-rud"),
    path("blogs/<int:pk>/like/", BlogLikeAPIView.as_view(), name="blog-like"),
]
