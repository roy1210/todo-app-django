from django.urls import path
# '.' MEANS right here, same lavel of folder
from . import views

urlpatterns = [
    # '' MEANS root. views.home MEANS ref the DEF imported in above. name='home' MEANS easier to create link later
    # path('address', view def, tag in html)
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name ='delete'),
    path('cross_off/<list_id>', views.cross_off, name ='cross_off'),
    path('uncross/<list_id>', views.uncross, name ='uncross'),
    path('edit/<list_id>', views.edit, name ='edit'),
]
