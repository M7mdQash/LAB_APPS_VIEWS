from django.urls import path
from . import views

app_name = "cars_rental"


urlpatterns = [
    path("", views.home, name="home_view"),
    path("about/",views.about, name="About_us_page"),
    path("password/generate",views.password_generate, name="password_generator")
]

