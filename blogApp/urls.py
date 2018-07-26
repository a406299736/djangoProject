from django.urls import path
from . import views

'''
新建 urls.py
'''
app_name = 'blog'
urlpatterns = [
    path('index', views.index, name='index'),
    path('detail', views.detail, name='dt'),
    path('page', views.PageView.as_view(), name='page'),
    # path('<int:question_id>/', views.dt, name='detail'),
    path('<int:pk>/', views.DtView.as_view(), name='detail'),     # 使用通用视图
    # path('results/<int:question_id>', views.results, name='result'),
    path('results/<int:pk>', views.ResultsView.as_view(), name='result'),
    path('vote/<int:question_id>', views.vote, name='vote'),
]