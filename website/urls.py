from django.urls import path
from . import views


urlpatterns = [
    #path('', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),

    path('record_list/', views.list_record, name='record_list'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.RecordCreateView.as_view(), name='add_record'),
    #path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('<int:pk>/convert/', views.ConvertToClientView.as_view(), name="convert"),

]
