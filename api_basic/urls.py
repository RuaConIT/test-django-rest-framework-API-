from django import urls
from django.urls import path, include
from .views import GenericAPIView, ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    # path('articles/', article_list, name = 'articles'),
    # path('articles/', ArticleAPIViews.as_view(), name = 'articles'),
    # path('detail/<int:pk>/', article_detail, name = 'detail'),
    # path('detail/<int:id>/', ArticleDetails.as_view(), name = 'detail'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name = 'generic')
]
