from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/', views.ProductDetailView.as_view(), name="detail"),
]
