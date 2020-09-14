from django.urls import path

from . import views


app_name = 'lovelyhalf'
urlpatterns = [
    path('', views.index, name='home'),
    path('/vote_page/<int:question_id>', views.vote_page, name='vote_page'),
    path('/vote/<int:question_id>', views.vote, name='vote'),
    path('/restaurant', views.restaurant_page, name='restaurant')
]
