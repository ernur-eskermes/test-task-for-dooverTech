from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    path('api/accounts/', include('accounts.api.urls')),
    path('api/products/', include('products.api.urls')),
    path('api/reviews/', include('reviews.api.urls')),
    path('api/cart/', include('carts.api.urls')),
    path('api/wishlist/', include('wishlist.api.urls')),
    path('api/orders/', include('orders.api.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path("api/__debug__/", include(debug_toolbar.urls))]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
