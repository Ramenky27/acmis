from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from ckeditor_uploader.views import upload, browse
from django.views.decorators.cache import never_cache

from cms.views.sitemap import CategoriesSitemap, PostsSitemap, StaticSitemap

from .views import post
from .views import comment
from .views import registration
from .views import profile
from .views import ajax
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from cms.forms.registration import RememberAuthenticationForm

from cms.views.rss import LatestEntriesFeed

sitemaps = {
	'categories': CategoriesSitemap,
  'static': StaticSitemap,
	'posts': PostsSitemap,
}

urlpatterns = [
  url(r'^$', post.post_list, name='post_list'),
  url(r'^post/new/$', post.post_new, name='post_new'),
  url(r'^post/(?P<pk>[0-9]+)/$', post.post_detail, name='post_detail'),

  url(r'^i18n/', include('django.conf.urls.i18n')),
  url(r'^post/(?P<pk>[0-9]+)/edit/$', post.post_edit, name='post_edit'),
  url(r'^post/(?P<pk>[0-9]+)/delete/$', post.post_delete, name='post_delete'),

  url(r'^post/(?P<pk>[0-9]+)/comment/new/$', comment.comment_new, name='comment_new'),
  url(r'^post/(?P<pk>[0-9]+)/comment(?P<cpk>[0-9]+)/reply/$', comment.comment_reply, name='comment_reply'),
  url(r'^post/(?P<pk>[0-9]+)/comment(?P<cpk>[0-9]+)/edit/$', comment.comment_edit, name='comment_edit'),
  url(r'^post/(?P<pk>[0-9]+)/comment(?P<cpk>[0-9]+)/delete/$', comment.comment_delete, name='comment_delete'),

  url(r'^author/(?P<author>\w+)?/$', post.post_list, name='author_list'),
  url(r'^author/(?P<author>\w+)/tags/(?P<tags>[\w\s\d\-_,]+)?/$', post.post_list, name='author_tags_list'),

  url(r'^category/(?P<category>\w+)?/$', post.post_list, name='category_list'),
  url(r'^category/(?P<category>\w+)/tags/(?P<tags>[\w\s\d\-_,]+)?/$', post.post_list, name='category_tags_list'),

  url(r'^tags/(?P<tags>[\w\s\d\-_,]+)/$', post.post_list, name='tag_list'),

#  url(r'^map/(?P<map_hash>\w+)/$', views.serve_map_file, name='map_file'),

  url(r'^accounts/login/$', registration.remember_login, {'template_name': 'registration/login.html', 'authentication_form': RememberAuthenticationForm}, name='auth_login'),
  url(r'^accounts/logout/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='auth_logout'),

  url(r'^accounts/activate/(?P<activation_key>[-:\w]+)/$', registration.activation, name='registration_activate'),
  url(r'^accounts/register/$', registration.registration, name='registration_register'),

  url(r'^accounts/password/change/$',
      auth_views.PasswordChangeView.as_view(
          success_url=reverse_lazy('auth_password_change_done')
      ),
      name='auth_password_change'),
  url(r'^accounts/password/change/done/$',
      auth_views.PasswordChangeDoneView.as_view(),
      name='auth_password_change_done'),
  url(r'^accounts/password/reset/$',
      auth_views.PasswordResetView.as_view(
          success_url=reverse_lazy('auth_password_reset_done')
      ),
      name='auth_password_reset'),
  url(r'^accounts/password/reset/complete/$',
      auth_views.PasswordResetCompleteView.as_view(),
      name='auth_password_reset_complete'),
  url(r'^accounts/password/reset/done/$',
      auth_views.PasswordResetDoneView.as_view(),
      name='auth_password_reset_done'),
  url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
      r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('auth_password_reset_complete')
        ),
        name='auth_password_reset_confirm'),
  url(r'^accounts/profile/(?P<username>\w+)/$', profile.profile, name='profile'),
  url(r'^accounts/profile/(?P<username>\w+)/edit/$', profile.profile_edit, name='profile_edit'),
  url(r'^accounts/userlist/$', profile.userlist, name='users_list'),
  url(r'^upload/', upload, name='ckeditor_upload'),
  url(r'^browse/', never_cache(browse), name='ckeditor_browse'),
  url(r'^ajax/tags/', ajax.get_simular_tags, name="get_simular_tags"),
  url(r'^messages/', include('django_messages.urls')),
  url(r'^sitemap\.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
  url(r'^latest/feed/', LatestEntriesFeed(), name="feed_latest"),
]

if settings.ENV == 'development':
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
