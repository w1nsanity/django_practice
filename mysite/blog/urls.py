from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    # обработчики приложения блога
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    # url-шаблон для обращения к списку статей, связанных с определенным тегом
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    # отправка email
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]