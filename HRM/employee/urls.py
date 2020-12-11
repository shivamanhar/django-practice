from django.urls import path

from . import views

# app_name more useful when we are using a multiple app in
# same project otherwise don't required to define app_name
app_name = 'employee' 

'''urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]'''
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
