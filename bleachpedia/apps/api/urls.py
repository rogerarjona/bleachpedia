from django.urls import path
from .views import shinigami_list, shinigami_detail, shinigami_add

urlpatterns = [
    path('shinigami/list/', shinigami_list, name="shinigami_list"),
    path('shinigami/add/', shinigami_add, name="shinigami_add"),
    path('shinigami/detail/<int:pk>/', shinigami_detail, name="shinigami_detail"),
]
