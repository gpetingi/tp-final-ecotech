# URLs del proyecto: acá conecto la dirección con la vista

from django.contrib import admin
from django.urls import path

from sustentabilidad.views import vista_panel_sustentabilidad

urlpatterns = [
    path("admin/", admin.site.urls),
    # la página principal muestra el panel de sustentabilidad
    path("", vista_panel_sustentabilidad, name="panel"),
]
