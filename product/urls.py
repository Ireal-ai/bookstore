from django.urls import path

from product.views import (
    BookView,
    OneBookView,
    GenreView,
    OneGenreView,
    BookVS,
    CreateCommentView,
    CreateRatingView,
    RecommendationView
)

app_name = 'product'

urlpatterns = [
    path('all', BookView.as_view(), name='books'),
    path('all2', BookVS.as_view({'get': 'list'}), name='books2'),
    path('add-comment', CreateCommentView.as_view(), name='add-comment'),
    path('rate', CreateRatingView.as_view(), name='add-rating'),
    path('recommendations', RecommendationView.as_view(), name='recommendations'),
    path('genres', GenreView.as_view(), name='genres'),
    path('genres/<id>', OneGenreView.as_view(), name='genre'),
    path('<id>', OneBookView.as_view(), name='book'),
]
