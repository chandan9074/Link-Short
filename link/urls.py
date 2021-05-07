from django.urls import path

from .views import CreatePublicLinkAPIView,RenderPublicURLAPIView,CreateUserLinkAPIView,EditUserLinkAPIView,UserUrlListAPIView,DeleteUserLinkAPIView

urlpatterns = [
    path("create_public_link/", CreatePublicLinkAPIView.as_view()),
    path("render_public_url/<str:str>/", RenderPublicURLAPIView.as_view()),
    path("create_user_link/", CreateUserLinkAPIView.as_view()),
    path("edit_user_link/<int:pk>/", EditUserLinkAPIView.as_view()),
    path("user_url_list/<int:pk>/", UserUrlListAPIView.as_view()),
    path("delete_user_link/<int:pk>/", DeleteUserLinkAPIView.as_view()),
]
