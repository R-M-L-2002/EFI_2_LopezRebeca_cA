# Endpoints API Documentacion

A continuación se describen los principales endpoints de la API 

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
```

## Autenticación y Registro

### Iniciar sesión

- **Método:** POST  
- **Endpoint:** `/login`

**Descripción:**  
Inicia sesión del usuario verificando las credenciales proporcionadas. Si las credenciales son correctas, establece la sesión.

**Ejemplo de cuerpo de solicitud:**
```html
{
    "username": "usuario123",
    "password": "contraseña"
}
```
### Registro de usuario

- **Método:** POST  
- **Endpoint:** `/register`

**Descripción:**  
Registra un nuevo usuario con un nombre de usuario y contraseña hasheada.

**Ejemplo de cuerpo de solicitud:**
```html
{
    "username": "nuevo_usuario",
    "password": "contraseña_segura"
}
```
### Gestion de Usuarios

- **Método:** POST  
- **Endpoint:** `/usuario`

**Descripción:**  
Lista todos los usuarios registrados. Solo accesible para administradores.

**Ejemplo de cuerpo de solicitud:**
```html
[
    {
        "id": 1,
        "username": "usuario123",
        "is_admin": true
    },
    {
        "id": 2,
        "username": "usuario456",
        "is_admin": false
    }
    // Otros usuarios
]

```
