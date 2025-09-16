from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review,
    name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', 
    views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/',
    views.delete_review, name='movies.delete_review'),
    path('survey/', views.survey_popup, name='survey_popup'),
    path('survey/list/', views.survey_list, name='survey_list'),

]