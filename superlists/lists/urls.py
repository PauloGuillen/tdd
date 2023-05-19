from django.urls import path
from superlists.lists.views import home_page


app_name = 'list'
urlpatterns = [
    path("", home_page, name='home'),
]
