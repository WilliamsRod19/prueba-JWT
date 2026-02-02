# core/permissions.py
from rest_framework.permissions import DjangoModelPermissions

class PermisosEstrictosDjango(DjangoModelPermissions):
    """
    Permiso global:
    - POST: requiere add_model
    - PUT: requiere change_model
    - DELETE: requiere delete_model
    - GET: requiere view_model (Esto es lo que agregamos)
    """
    def __init__(self):
        super().__init__()
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']