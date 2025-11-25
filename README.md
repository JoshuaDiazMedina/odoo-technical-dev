# Odoo technical modules


# Update de módulo - desarrollo

Ejemplo:

```
:~/INDAWS/odoo19-indaws$ ./odoo/odoo-bin -d odoo19 --addons-path="enterprise/,odoo-technical-dev/" -u estate
```

# Real Estate (estate)

Módulo técnico de ejemplo para gestionar propiedades inmobiliarias.

Resumen
- Nombre del módulo: Real Estate
- Versión: definida en [`odoo-technical-dev/estate/__manifest__.py`](odoo-technical-dev/estate/__manifest__.py)
- Autor: Joshua Diaz
- Dependencias principales: `crm` (ver manifiesto)

Qué hace
- Modelo principal de propiedades: [`estate_property.EstateProperty`](odoo-technical-dev/estate/models/estate_property.py)
  - Campos: name, state, price, selling_price, availability_date, bedrooms, property_type_id, buyer_id, ...
- Mixin de ejemplo: [`estate_mixin.EstateMixin`](odoo-technical-dev/estate/models/estate_mixin.py)
- Demo con datos de ejemplo: [demo/demo.xml](odoo-technical-dev/estate/demo/demo.xml)

Estructura importante
- Manifest: [odoo-technical-dev/estate/__manifest__.py](odoo-technical-dev/estate/__manifest__.py)
- Modelos: [odoo-technical-dev/estate/models/estate_property.py](odoo-technical-dev/estate/models/estate_property.py)
- Models init: [odoo-technical-dev/estate/models/__init__.py](odoo-technical-dev/estate/models/__init__.py)

