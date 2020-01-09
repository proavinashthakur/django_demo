from django.urls import path
from . import views
urlpatterns = [
    path("add-data", views.add_data, name="add-data"),

]
