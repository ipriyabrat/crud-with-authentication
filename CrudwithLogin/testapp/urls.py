 
 
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('',views.home_view),
    # path('listview/',views.BookListView.as_view(),name='list'),
    path('listview/',views.BookRetriveView,name='list'),
    path('<int:pk>',views.BookDetailsView.as_view(),name='detail'),
    path('create/',views.BookCeeateView.as_view()),
    path('update/<int:pk>',views.BookUpdateView.as_view()),
    path('delete/<int:pk>',views.BookDeleteView.as_view()),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout_view),
    path('signup/',views.signup_view),
    
]