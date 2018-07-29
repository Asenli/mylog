from django.urls import path
from . import views
# http://localhost:8000/blog/1

# #总路由
# http://localhost:8000

urlpatterns = [
   path('update_comment',views.update_comment,name='update_comment')
]