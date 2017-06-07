from django.conf.urls import url
import views

urlpatterns = [
    url(r'^add(\d+)_(\d+)/$', views.add),
    url(r'^$', views.list),
    url(r'^count_change/$', views.count_change),
]
