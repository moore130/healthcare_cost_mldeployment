from django.urls import path
from . import views

app_name = 'estimator'

urlpatterns = [
    path('', views.estimator, name ='estimator_page'),
    path('estimate/', views.estimate_chances, name = 'submit_estimation'),
    path('results/', views.view_results, name='results'),

]