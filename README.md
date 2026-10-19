# Pruebas de API: creación de usuarios en Urban Grocers

## Descripción del proyecto

Proyecto de automatización de pruebas de API para validar el proceso de creación de usuarios en Urban Grocers, con énfasis en las reglas de validación del parámetro `firstName`.

El objetivo es comprobar cómo responde el servicio ante datos válidos e inválidos, verificar los códigos de estado HTTP y validar la información devuelta durante la creación de usuarios.

## Objetivo de las pruebas

Evaluar el comportamiento del endpoint de creación de usuarios mediante casos positivos y negativos, comprobando que las respuestas de la API coincidan con los resultados esperados para cada escenario.

## Mi contribución

- Diseñé y ejecuté casos de prueba para diferentes valores de `firstName`.
- Utilicé aserciones de Pytest para validar los códigos de estado HTTP.
- Comprobé la presencia de un `authToken` en las respuestas exitosas.
- Evalué el comportamiento de la API frente a valores que deberían ser rechazados.
- Analicé los resultados de ejecución para identificar diferencias entre el comportamiento esperado y el obtenido.

## Herramientas utilizadas

- **Python:** lenguaje utilizado para desarrollar las pruebas.
- **Pytest:** ejecución y organización de los casos de prueba.
- **Requests:** envío de solicitudes HTTP a la API.
- **Git y GitHub:** control de versiones y documentación del proyecto.
- **PyCharm:** entorno de desarrollo.

## Estrategia y escenarios de prueba

Las pruebas se enfocan en la validación del parámetro `firstName` durante la creación de usuarios.

| Categoría | Escenarios evaluados |
|---|---|
| Longitud del nombre | Nombres de 1, 2, 4, 6 y 15 caracteres |
| Espacios | Nombre que contiene un espacio |
| Símbolos especiales | Nombre con caracteres especiales |
| Números | Nombre compuesto por números |

### Validaciones positivas

- Verificar que la API responda con HTTP `201` cuando la creación del usuario sea exitosa.
- Comprobar que la respuesta incluya un `authToken` no vacío.
- Validar que el usuario aparezca una sola vez en la tabla de usuarios.

### Validaciones negativas

- Verificar que la API responda con HTTP `400` cuando los datos enviados no cumplan las reglas de validación.
- Comprobar el comportamiento del servicio frente a nombres con espacios, símbolos especiales y números.

## Estructura del proyecto

- `configuration.py`: configuración de la URL del servicio y las rutas de la API.
- `create_user_test.py`: funciones auxiliares y casos de prueba para la creación de usuarios.
- `sender_stand_request.py`: funciones para enviar solicitudes a la API.
- `data.py`: datos utilizados para construir las solicitudes.
- `main.py`: archivo de entrada del proyecto, si se utiliza para ejecutar las pruebas.

## Cómo ejecutar las pruebas

1. Instalar Python.
2. Instalar las dependencias necesarias:

   ```bash
   pip install pytest requests
   ```

3. Iniciar el servidor de Urban Grocers desde la plataforma de TripleTen y actualizar `URL_SERVICE` en `configuration.py` si la dirección ha cambiado.
4. Abrir una terminal en la carpeta del proyecto y ejecutar:

   ```bash
   pytest
   ```

## Resultados de ejecución

En una ejecución realizada el 19 de octubre de 2026 se obtuvieron los siguientes resultados:

- **8 pruebas aprobadas.**
- **1 prueba fallida.**
- **Duración aproximada:** 8,6 segundos.

La prueba fallida fue `test_create_user_has_space_in_first_name_get_error_response`.

- **Resultado esperado:** HTTP `400`.
- **Resultado obtenido:** HTTP `201`.

El resultado indica una diferencia entre el comportamiento esperado y la respuesta de la API para un nombre que contiene espacios. Este hallazgo requiere revisión para determinar si corresponde a una regla de validación no aplicada por el servicio o a una expectativa que debe confirmarse.

Los resultados corresponden a una ejecución puntual y pueden variar según el estado del servidor y los datos utilizados.

## Aprendizajes

Este proyecto permitió practicar el diseño de pruebas de API, la preparación de solicitudes HTTP, el uso de aserciones con Pytest y la validación de respuestas. También reforzó la importancia de analizar los resultados reales, documentar las diferencias entre el resultado esperado y el obtenido, y comunicar los hallazgos de manera clara.

## Repositorio

[Ver el proyecto API Stand Tests en GitHub](https://github.com/juliadiaz-blip/api_stand_tests)
