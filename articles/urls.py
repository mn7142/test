from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'articles'),
    # /articles/<int:article_id>
    path('<int:article_id>/' , views.single , name = 'article')
]

