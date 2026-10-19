# Pruebas API: creación de usuarios en Urban Grocers

## Descripción del proyecto

Proyecto de automatización de pruebas de API para validar el parámetro `firstName` durante la creación de usuarios en Urban Grocers.

El objetivo es comprobar que el servicio acepte nombres válidos y rechace valores que no cumplen con las condiciones esperadas.

## Objetivo de las pruebas

Verificar las respuestas de la API al enviar diferentes valores para `firstName`, comprobar los códigos de estado HTTP y validar la información devuelta cuando la creación del usuario es exitosa.

## Herramientas utilizadas

- Python
- Pytest
- Requests
- Git y GitHub

## Estrategia y escenarios de prueba

El proyecto contiene pruebas positivas y negativas que cubren los siguientes escenarios:

| Categoría | Escenarios |
|---|---|
| Longitud del nombre | Nombres de 1, 2, 4, 6 y 15 caracteres |
| Espacios | Nombre que contiene un espacio |
| Símbolos especiales | Nombre con caracteres especiales |
| Números | Nombre compuesto por números |

### Validaciones realizadas

**Pruebas positivas:**
- Verificar que la API responda con código HTTP `201`.
- Comprobar que la respuesta incluya un `authToken` no vacío.
- Validar que el usuario aparezca una sola vez en la tabla de usuarios.

**Pruebas negativas:**
- Verificar que la API responda con código HTTP `400` para los valores no válidos.

## Estructura del proyecto

- `create_user_test.py`: contiene las funciones auxiliares y los casos de prueba.
- `sender_stand_request.py`: contiene las solicitudes utilizadas para interactuar con la API.
- `data.py`: contiene los datos utilizados para construir el cuerpo de la solicitud.

## Cómo ejecutar las pruebas

1. Instalar Python.
2. Instalar las dependencias necesarias:

   ```bash
   pip install pytest requests
   ```

3. Ejecutar las pruebas desde la carpeta del proyecto:

   ```bash
   pytest
   ```

## Resultados

Los resultados deben registrarse después de ejecutar las pruebas. Este README describe las validaciones implementadas en el código, pero no afirma que todas hayan pasado.

## Aprendizajes

Este proyecto permitió practicar el diseño de pruebas de API, la validación de códigos de estado HTTP, el uso de aserciones con Pytest y la comprobación de datos devueltos por un servicio.

