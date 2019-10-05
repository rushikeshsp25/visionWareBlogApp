from django.urls import path,include
from . import views

# namespace
app_name = 'home'
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('',views.index,name='index'),
    path('posts/id/<int:post_id>/',views.posts_by_id,name='posts_by_id'),
    path('posts/author/',views.posts_by_author,name='posts_by_author'),
    path('posts/archives/monthly/',views.posts_archive_monthly,name='posts_archive_monthly'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginUser,name='login'),
    path('addpost/',views.addPost,name='add_post'),
    path('logout/',views.logoutUser,name='logout'),
    path('contact_us/',views.contact_us,name='contact_us'),
]