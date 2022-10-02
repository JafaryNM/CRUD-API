from django.urls import path
from .views import PersonDetail,PersonUpdate,PersonDelete

urlpatterns = [
    path('', PersonDetail.as_view()),
    path('update/<int:pk>',PersonUpdate.as_view()),
    path('delete/<int:pk>',PersonDelete.as_view()),
]
