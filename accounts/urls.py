from django.urls import path
from .views import logout,registerPage,loginPage, home,products,updateOrder,customer,createOrder,deleteOrder

urlpatterns = [
    path('',home, name='home'),
    path("login/",loginPage,name='login'),
    path("logout/",logout,name='logout'),
    path("register/",registerPage,name='register'),
    path("products/",products,name='products'),
    path("customers/<str:pk_test>/",customer,name='customers'),
    path("create_order/<str:pk>/",createOrder , name="create_order"),
    path("update_order/<str:pk>/",updateOrder , name="update_order"),
    path("delete_order/<str:pk>/",deleteOrder , name="delete_order"),
]

