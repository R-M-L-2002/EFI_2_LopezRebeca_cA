# Endpoints API Documentacion

A continuación se describen los principales endpoints de la API relacionados con la gestión de accesorios.

## Accesorios

### Listar todos los accesorios

- **Método:** GET  
- **Endpoint:** `/accesorios`

**Descripción:**  
Lista todos los accesorios disponibles.

**Ejemplo de respuesta:**

```html
[
    {
        "id": 1,
        "tipo": "Cargador",
        "modelo_id": 3
    },
    {
        "id": 2,
        "tipo": "Audífonos",
        "modelo_id": 2
    }
    // Otros objetos de accesorio
]

