from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.http import JsonResponse

from tasks.views import AdminTaskView, PublicTaskListCreateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Root welcome API
def api_root(request):
    return JsonResponse({"message": "Welcome to the Cloud Task Manager API"})

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API documentation for the Task Manager system",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@taskmanager.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-task/<int:pk>/', AdminTaskView.as_view(), name='admin-task'),

    # REST API endpoints
    path('api/', api_root),
    path('api/tasks/', include('tasks.api_urls')),
    path('auth/', include('rest_framework.urls')),
    path('public-tasks/', PublicTaskListCreateView.as_view(), name='public-tasks'),
    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Task app UI views
    path('', include('tasks.urls')),  # UI, login, dashboard, etc.
    path('accounts/', include('django.contrib.auth.urls')),  # Optional auth routes
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
