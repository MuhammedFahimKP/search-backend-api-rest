from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/',views.ProductDetailView.as_view(),name="product-detail"),
    path('create/',views.ProductCreateView.as_view()),
    path('list/',views.ProductListView.as_view()),
    path('',views.ProductListCreateView.as_view()),
    path('update/<int:pk>/',views.ProductUpdateView.as_view(),name="product-edit"),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view()),
]
