from django.urls import path
from .views import HomeView, PostView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/post/<int:pk>', PostView.as_view(), name='post_details'),
    path('post/add', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/add', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category')
]
