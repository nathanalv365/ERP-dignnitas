# ERP-dignnitas

## Objetivo general
Construir un ERP modular para gestionar operaciones básicas de una organización (ventas, inventario y compras) con trazabilidad y reportes simples.

## Objetivos iniciales (MVP)
1. **Autenticación básica** de usuarios con roles (admin y operador).
2. **Gestión de productos** (crear, listar, editar, desactivar).
3. **Gestión de inventario** (entradas, salidas y stock actual).
4. **Registro de ventas** con detalle de ítems y total.
5. **Reporte simple** de ventas por rango de fechas.

## Criterios de validación del MVP
- Todas las operaciones CRUD principales responden correctamente.
- El stock se actualiza de forma consistente en cada movimiento.
- El reporte de ventas coincide con los datos registrados.
- El flujo mínimo (login → alta producto → movimiento stock → venta → reporte) es ejecutable.
