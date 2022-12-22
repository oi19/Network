from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),



    # API Routes
    path("post", views.createPost, name="post"),
    path("post/<str:type>", views.getPosts, name="getPost"),
    path("post/body/<int:id>", views.updatePost, name="updatePost"),
    path("post/likes/<int:id>", views.updateLikes, name="updatLikes"),
    path("user/<int:id>", views.userProfile, name="userProfile"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
