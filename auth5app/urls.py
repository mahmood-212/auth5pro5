from django.conf.urls import url
from auth5app import views

# Template urls!
app_name = 'auth5app'


urlpatterns =[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),

]