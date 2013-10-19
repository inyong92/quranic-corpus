from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
  '',
  # Examples:
  # url(r'^$', 'website.views.home', name='home'),
  # url(r'^website/', include('website.foo.urls')),

  # Uncomment the admin/doc line below to enable admin documentation:
  # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  url(r'^admin/', include(admin.site.urls)),

  # Registration
  url(r'^accounts/', include('registration.backends.default.urls')),

  # Morphology
  url(r'^morphology/', include('morphology.urls')),

  # Morphology
  url(r'^setup/', include('setup.urls'))
)
