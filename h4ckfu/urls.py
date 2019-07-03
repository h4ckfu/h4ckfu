from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import home.views
import work.views
import cert.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('work/', work.views.work, name='work'),
    path('cert/', cert.views.cert, name='cert'),
    path('blog/', include('blog.urls')),
    #url(r'^path/to/blog/', include('wordpress.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)