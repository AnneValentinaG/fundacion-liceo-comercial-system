# Fundación Liceo Comercial Ciudad De El Bordo - Plataforma Institucional

Plataforma digital institucional orientada a fortalecer la presencia web de la Fundación Liceo Comercial Ciudad De El Bordo y proporcionar herramientas digitales para apoyar procesos administrativos, gestión documental, seguimiento de información y comunicación institucional.

## Descripción del proyecto

El proyecto surge a partir del diagnóstico realizado sobre el sitio web institucional y de la identificación de diferentes necesidades relacionadas con la gestión de información, procesos administrativos y comunicación digital de la Fundación.

Inicialmente se realizó un diagnóstico del sitio existente y posteriormente se desarrolló un prototipo funcional para validar la estructura, organización y presentación de la información institucional.

A partir de este proceso se definió una arquitectura híbrida, manteniendo los sitios públicos mediante WordPress y Elementor y desarrollando de manera independiente una plataforma administrativa privada mediante Django y PostgreSQL.

Esta estrategia permite conservar la facilidad de administración de los contenidos públicos y, al mismo tiempo, incorporar herramientas internas con mayor capacidad para manejar usuarios, información estructurada y procesos administrativos.

## Objetivo

Diseñar y desarrollar progresivamente un ecosistema digital institucional que permita fortalecer la presencia web de la Fundación y proporcionar herramientas tecnológicas para apoyar la gestión administrativa, documental y comunicacional.

# Ecosistema digital institucional

Actualmente el proyecto se encuentra organizado en tres componentes principales:

## 1. Sitio web de la Fundación

Desarrollado mediante:

- WordPress.
- Elementor.
- Hostinger.

Sitio público principal:

https://fundacionliceocomercial.com.co/

Este espacio está destinado a presentar información relacionada con:

- Identidad institucional.
- Historia y trayectoria.
- Programas y servicios.
- Proyectos.
- Impacto.
- Territorios.
- Información de contacto.
- Actividades institucionales.

## 2. Sitio web de la Institución Educativa

También desarrollado mediante WordPress y Elementor.

Sitio público:

https://institucioneducativa.fundacionliceocomercial.com.co/

Este espacio permite organizar de manera independiente la información correspondiente a la Institución Educativa de la Fundación, incluyendo contenidos dirigidos a estudiantes, familias y comunidad educativa.

## 3. Plataforma administrativa interna

Desarrollada mediante:

- Python.
- Django.
- Django REST Framework.
- PostgreSQL.
- HTML.
- CSS.

La plataforma administrativa se encuentra orientada al desarrollo de herramientas internas y actualmente funciona en entorno local de desarrollo.

Se proyecta su publicación posterior mediante un subdominio institucional.

Ejemplo:

app.fundacionliceocomercial.com.co

# Arquitectura tecnológica

La solución utiliza una arquitectura híbrida:

Sitios públicos
WordPress + Elementor
        |
        |
        +----------------------+
                               |
                               v
                    Plataforma administrativa
                           Django
                               |
                               v
                          PostgreSQL

Esta separación permite que los contenidos públicos y las herramientas administrativas puedan evolucionar de manera independiente.

# Funcionalidades implementadas

Durante el desarrollo se incorporaron progresivamente las siguientes funcionalidades:

## Autenticación

- Inicio de sesión.
- Cierre de sesión.
- Protección de páginas internas.
- Organización inicial de usuarios mediante grupos.

## Dashboard institucional

Panel principal desde el cual se organizan los diferentes módulos de la plataforma.

Actualmente contempla accesos a:

- Administración de usuarios.
- Gestión documental.
- Contratos.
- Publicaciones en redes sociales.
- Métricas.
- Seguimiento de comunicaciones.
- Asistente de contenido.

## Gestión documental

Permite:

- Registrar documentos.
- Consultar documentos almacenados.
- Visualizar información detallada.
- Manejar estados.
- Asignar responsables.
- Asociar archivos digitales.
- Mantener información de radicación.

## Gestión de contratos

Permite:

- Registrar contratos.
- Consultar contratos existentes.
- Visualizar información individual.
- Manejar estados contractuales.
- Registrar fechas importantes.
- Asociar un responsable.
- Relacionar documentación contractual.

## Publicaciones en redes sociales

Permite registrar información relacionada con:

- Red social.
- Tema.
- Contenido.
- Fecha de publicación.
- Tipo de contenido.
- Estado.
- Enlace de publicación.

## Métricas digitales

Permite registrar y consultar:

- Alcance.
- Reacciones.
- Comentarios.
- Compartidos.
- Guardados.
- Impresiones.
- Total de interacciones.
- Tasa básica de interacción.

## Asistente local de contenido

Se desarrolló una primera versión de un asistente local orientado a apoyar la creación de contenido institucional.

El usuario puede indicar:

- Tema.
- Red social.
- Objetivo.
- Descripción de la necesidad.

A partir de esta información la aplicación genera una propuesta que incluye:

- Texto sugerido.
- Hashtags.
- Idea visual.
- Recomendación de comunicación.

La herramienta funciona mediante lógica local implementada en Python y no depende obligatoriamente de servicios externos pagos.

# Funcionalidades proyectadas

Algunas características quedaron preparadas para etapas posteriores:

- Publicación de Django en infraestructura institucional.
- Uso del subdominio app.fundacionliceocomercial.com.co.
- Implementación completa del módulo de Seguimiento de comunicaciones.
- Recuperación de contraseña mediante correo electrónico.
- Ampliación de roles y permisos.
- Automatización de reportes.
- Integración automática con métricas de redes sociales.
- Integración opcional con servicios externos de inteligencia artificial.
- Generación automatizada de piezas gráficas.

# Base de datos

La plataforma administrativa utiliza PostgreSQL.

La base de datos principal utilizada durante el desarrollo es:

fundacion_plataforma

Entre las estructuras principales se encuentran:

- Usuarios.
- Documentos.
- Contratos.
- Documentación relacionada con contratos.
- Publicaciones.
- Métricas.

Django administra la estructura mediante modelos y migraciones.

# Seguridad

Durante el desarrollo se implementaron medidas básicas de seguridad, entre ellas:

- Autenticación de usuarios.
- Restricción de acceso a páginas privadas.
- Organización inicial mediante grupos.
- Uso de variables de entorno.
- Protección de credenciales.
- Exclusión del archivo `.env` del repositorio.
- Separación de información privada y código fuente.
- Respaldo de PostgreSQL.
- Manejo de la clave privada de Django mediante variables de entorno.

# Estructura general del proyecto

La estructura principal del repositorio es aproximadamente:

fundacion-plataforma/
│
├── backend/
│   ├── config/
│   ├── core/
│   ├── usuarios/
│   ├── documentos/
│   ├── contratos/
│   ├── publicaciones/
│   ├── metricas/
│   ├── asistente_ia/
│   ├── templates/
│   ├── static/
│   └── manage.py
│
├── docs/
│   ├── arquitectura/
│   ├── diagramas/
│   └── requerimientos/
│
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt

# Tecnologías utilizadas

## Desarrollo

- Python
- Django
- Django REST Framework
- HTML
- CSS

## Base de datos

- PostgreSQL
- pgAdmin

## Sitios públicos

- WordPress
- Elementor
- Hostinger

## Control de versiones

- Git
- GitHub

## Herramientas de desarrollo

- Visual Studio Code
- Git Bash

