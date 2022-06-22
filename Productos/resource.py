from import_export import resources

from Productos.models import Catalogo


class CatalogoResource(resources.ModelResource):
    class Meta:
        model=Catalogo