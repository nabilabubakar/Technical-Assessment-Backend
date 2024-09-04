from django.urls import path, re_path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Api Documentation",

    ),
    public=True,
)

urlpatterns = [
    path('api/items/', views.ListItem.as_view(), name='list-items'),
    path('api/items/<int:pk>/', views.GetItem.as_view(), name='get-item'),
    path('swagger<format>.json|.yaml$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
