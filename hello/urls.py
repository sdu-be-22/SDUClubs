
from ast import Or
from operator import index
from unicodedata import name
from django import views
from django.urls import path
from .views import AddCategoryView, ArticleDetailView, CategoryView, TaskList,TaskCreate,TaskCreateMusic,TaskCreateArt,TaskCreateVision,TaskCreateDebate, dombyra,music, logout_user
# adding Ali
from . import views
from .views import index

# kama
from django.urls import path
from .views import HomeView, AddBlogView, UpdatePostView, DeleteViewPost
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.login_user, name='login'),
    path('main/',TaskList.as_view(), name = 'tasks'),
    path('task-create/' , TaskCreate.as_view(),name='task-create'),
    path('task-music/',TaskCreateMusic.as_view(),name='task-music'),
    path('task-art/',TaskCreateArt.as_view(),name='task-art'),
    path('task-vision/',TaskCreateVision.as_view(),name='task-vision'),
    path('task-debate/',TaskCreateDebate.as_view(),name='task-debate'),
    path('main/hi', index , name='index'),
    path('dombyra', dombyra, name ="dombyra"),
    path('music', music, name ="music"),
    path('log_out', logout_user, name = "logout_user"),
    
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),

    
    # kama
    path('see_blog/', HomeView.as_view(), name="home"),
    path('blog/<int:blog_id>', views.details, name='blog_detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('blog/<int:pk>/remove', DeleteViewPost.as_view(), name = "delete_post"),
    path('add_category2/', views.create_view, name='add_category2'),


   

]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


    # # path('main/hi', index , name='index'),
    # path('', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password', views.change_password, name='change_password'),
    # path('home2/', views.home2, name = "home2"),


    # path('', views.WebpageLoginView.as_view(), name='login'),
    # path('main/',TaskList.as_view(), name = 'tasks')  ,
    # path('task-create/' , TaskCreate.as_view(),name='task-create'),
    # path('task-music/',TaskCreateMusic.as_view(),name='task-music'),
    # path('task-art/',TaskCreateArt.as_view(),name='task-art'),
    # path('task-vision/',TaskCreateVision.as_view(),name='task-vision'),
    # path('task-debate/',TaskCreateDebate.as_view(),name='task-debate'),




    
    
    
    

