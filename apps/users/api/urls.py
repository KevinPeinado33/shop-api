from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view
""" from apps.users.api.api import UserApiView """

""" path('user/', UserApiView.as_view(), name = 'user_api') """
urlpatterns = [

    path('user/', user_api_view, name = 'user_api'),
    
    path('user/<int:pk>/', user_detail_api_view, name = 'user_detail_api_view'),

]