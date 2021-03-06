from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^add_category/$', views.add_category, name='add_category'), # new mapping
        #url(r'^add_page/$', view.add_page, name='add_page'),
        #url(r'^search/$', views.search, name='search'),
        url(r'^goto/$', views.track_url, name='goto'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),) # New!

        
