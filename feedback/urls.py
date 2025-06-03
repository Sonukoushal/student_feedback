from django.contrib import admin
from django.urls import path
from feedback.views import feedback_view,feedback_list

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',feedback_view,name='feedback_form'),
    path('feedbacks/',feedback_list,name='feedback_list'),
]