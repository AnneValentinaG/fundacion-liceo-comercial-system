
## Fundación Liceo Comercial Ciudad De El Bordo  Plataforma

Plataforma digital institucional orientada a fortalecer la presencia web de la Fundación Liceo Comercial Ciudad De El Bordo y proporcionar herramientas digitales para apoyar procesos administrativos, gestión documental, seguimiento de información y comunicación institucional.

## Descripción del proyecto

El proyecto surge a partir del diagnóstico realizado sobre el sitio web institucional y de la identificación de diferentes necesidades relacionadas con la gestión de información, procesos administrativos y comunicación digital de la Fundación.

Inicialmente se desarrolló un prototipo funcional para validar la estructura y presentación del sitio institucional.

A partir de dicha experiencia se plantea una evolución tecnológica basada en una arquitectura híbrida, en la cual el sitio web público continuará utilizando WordPress y Elementor, mientras que las funcionalidades administrativas y personalizadas serán desarrolladas mediante una aplicación independiente.

Esta estrategia permite conservar la infraestructura y el trabajo realizado en el sitio institucional actual, mientras se construye progresivamente una plataforma con mayor capacidad de personalización y control.

## Objetivo

Diseñar y desarrollar progresivamente un ecosistema digital institucional que permita fortalecer el sitio web de la Fundación y proporcionar herramientas tecnológicas para apoyar la gestión administrativa, documental y comunicacional.

## Necesidades identificadas

Durante el proceso de análisis se identificaron necesidades relacionadas con:

- Sitio web institucional.
- Administración de contenidos.
- Gestión de usuarios y permisos.
- Gestión documental.
- Seguimiento de información.
- Formularios digitales.
- Visualización de información mediante dashboards.
- Seguimiento de publicaciones y métricas digitales.
- Automatización de procesos.
- Apoyo mediante herramientas de inteligencia artificial.

Estas necesidades serán abordadas progresivamente durante las diferentes etapas del proyecto.

## Arquitectura propuesta

El proyecto contempla una arquitectura híbrida compuesta inicialmente por los siguientes elementos:

### Sitio web público

**WordPress + Elementor**

Será utilizado para la presentación y administración del contenido público de la Fundación.

Incluye las secciones institucionales destinadas a visitantes, comunidad educativa y público general.

### Aplicación interna

**Django**

Se plantea como tecnología para desarrollar una aplicación privada orientada a funcionalidades administrativas y procesos personalizados.

Entre las funcionalidades proyectadas se encuentran:

- Gestión de usuarios.
- Roles y permisos.
- Gestión documental.
- Formularios.
- Seguimiento de información.
- Dashboard.
- Gestión de publicaciones.
- Métricas.
- Automatización.
- Integración de herramientas de inteligencia artificial.

### Base de datos

**PostgreSQL**

Se selecciona inicialmente como sistema de gestión de base de datos para almacenar de forma estructurada la información correspondiente a la aplicación interna.

## Módulos proyectados

La plataforma se organizará progresivamente en diferentes módulos:

### 1. Sitio institucional

Espacio público destinado a presentar:

- Información institucional.
- Programas.
- Proyectos.
- Noticias.
- Información de contacto.
- Información educativa.

### 2. Administración

Módulo privado para:

- Usuarios.
- Roles.
- Permisos.
- Configuración.
- Administración de información.

### 3. Gestión documental

Orientado a organizar y controlar información institucional como:

- Contratos.
- Actas.
- Informes.
- Órdenes de compra.
- Soportes.
- Otros documentos institucionales.

### 4. Seguimiento y reportes

Permitirá proyectar herramientas para:

- Seguimiento de información.
- Indicadores.
- Estadísticas.
- Reportes.
- Visualización mediante dashboards.

### 5. Comunicación digital

Módulo orientado al seguimiento y organización de actividades relacionadas con la comunicación institucional y redes sociales.

### 6. Automatización e inteligencia artificial

Como componente de innovación se proyecta incorporar herramientas de inteligencia artificial para apoyar procesos de generación y planificación de contenido institucional.

## Seguridad

La arquitectura propuesta contempla la implementación progresiva de mecanismos básicos de seguridad, entre ellos:

- Autenticación de usuarios.
- Control de acceso mediante roles.
- Validación de información.
- Protección de datos.
- Gestión de permisos.
- Copias de seguridad.
- Protección de información institucional.

Las medidas específicas serán implementadas durante las etapas posteriores del desarrollo.

## Estructura del repositorio

Actualmente el proyecto se organiza de la siguiente manera:

fundacion-plataforma/
│
├── README.md
├── .gitignore
│
└── docs/
    ├── arquitectura/
    ├── diagramas/
    └── requerimientos/