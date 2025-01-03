from django.urls import path 
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('insert',views.insert,name='insert'),
    path('view',views.view),
    path('contact/delete/<int:id>', views.delete, name='delete'),
    path('contact/', views.edit1, name='edit1'),  # Corrected the view name
    path('update/<int:id>/', views.update, name='update_contact'), 
]