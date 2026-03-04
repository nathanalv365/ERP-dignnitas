# Plan de pruebas del MVP

## 1. Objetivos cubiertos
- Autenticación por roles.
- Gestión de productos.
- Gestión de inventario.
- Registro de ventas.
- Reporte de ventas por fechas.

## 2. Casos de prueba

| ID | Objetivo | Precondiciones | Pasos | Resultado esperado |
|----|----------|----------------|-------|--------------------|
| CP-001 | Login con rol admin | Usuario admin creado | 1. Abrir login 2. Ingresar credenciales válidas | Acceso concedido con permisos de admin |
| CP-002 | Alta de producto | Usuario autenticado | 1. Ir a productos 2. Crear producto con datos válidos | Producto visible en listado |
| CP-003 | Entrada de inventario | Producto existente | 1. Registrar entrada de 10 unidades | Stock aumenta en 10 |
| CP-004 | Venta con descuento de stock | Producto con stock > 0 | 1. Crear venta de 2 unidades | Venta registrada y stock disminuye en 2 |
| CP-005 | Reporte por rango de fechas | Ventas registradas | 1. Seleccionar rango 2. Ejecutar reporte | Totales coinciden con ventas del rango |

## 3. Evidencia
- Capturas y/o logs de ejecución por cada caso de prueba.

## 4. Próximos pasos
1. Convertir casos manuales a pruebas automatizadas.
2. Integrar ejecución en CI.
