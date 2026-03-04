# ERP Fundación Dignitas

Este repositorio define la visión inicial de un ERP modular y escalable para **Fundación Dignitas**.

## Objetivo del sistema

Construir una aplicación robusta que permita:

- Administrar inventario (entradas, salidas, stock mínimo, trazabilidad).
- Generar certificados con plantillas configurables y firma digital.
- Agregar nuevas funcionalidades por módulos sin afectar lo ya construido.
- Fortalecer continuamente los procesos actuales con métricas y auditoría.

## Propuesta funcional (MVP)

### 1) Inventario

- Catálogo de productos/insumos con categorías.
- Gestión de bodegas y ubicaciones.
- Movimientos de inventario (ingreso, ajuste, transferencia, salida).
- Alertas de stock mínimo.
- Kardex por producto.

### 2) Certificados

- Plantillas de certificados por tipo (beneficiario, donación, participación, etc.).
- Variables dinámicas (nombre, cédula, fecha, código único).
- Generación en PDF.
- Historial y reimpresión.
- Validación por código/QR.

### 3) Seguridad y control

- Usuarios, roles y permisos granulares.
- Bitácora de acciones (auditoría).
- Gestión de sesiones y políticas de contraseña.

### 4) Reportes

- Reportes de inventario por fecha, categoría y bodega.
- Reportes de certificados emitidos.
- Exportación a Excel/PDF.

## Arquitectura recomendada

Para crecer en el tiempo sin rehacer el sistema:

- **Backend API**: arquitectura modular (monolito modular inicialmente).
- **Base de datos relacional**: PostgreSQL.
- **Frontend web**: panel administrativo responsivo.
- **Autenticación**: JWT + refresh tokens.
- **Archivos**: almacenamiento de PDFs y plantillas.
- **Observabilidad**: logs estructurados y monitoreo básico.

## Módulos evolutivos (fase 2+)

- Compras y proveedores.
- Donaciones y trazabilidad por proyecto.
- CRM social (beneficiarios, atenciones, seguimiento).
- Gestión documental.
- Integraciones contables/facturación.
- Tablero de indicadores (KPIs).

## Modelo de implementación sugerido

1. **Descubrimiento (1–2 semanas)**
   - Levantamiento de procesos actuales.
   - Priorización de requerimientos.
   - Diseño del MVP.

2. **Construcción MVP (6–10 semanas)**
   - Inventario + certificados + seguridad + reportes base.
   - Pruebas funcionales con usuarios clave.

3. **Estabilización (2 semanas)**
   - Ajustes de rendimiento.
   - Fortalecimiento de reglas de negocio.
   - Capacitación inicial.

4. **Evolución continua**
   - Incorporación de nuevos módulos por iteraciones.
   - Roadmap trimestral.

## Requisitos no funcionales clave

- Escalabilidad modular.
- Seguridad de datos personales.
- Trazabilidad completa de operaciones.
- Disponibilidad y respaldos automáticos.
- Mantenibilidad (documentación + pruebas).

## Próximos pasos recomendados

- Definir stack tecnológico final (por ejemplo: NestJS + PostgreSQL + React).
- Elaborar historias de usuario por módulo.
- Diseñar esquema de base de datos inicial.
- Crear prototipo de UI y flujo de certificados.
- Configurar repositorio con CI/CD y estándares de calidad.
