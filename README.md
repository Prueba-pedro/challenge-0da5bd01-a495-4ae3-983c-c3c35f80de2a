# Desarrollo de una API REST para gestión de cuentas bancarias

La empresa necesita una API REST para gestionar cuentas bancarias en un entorno de fintech. La API debe permitir la creación, lectura, actualización y eliminación de cuentas. Además, debe implementar autenticación y autorización utilizando JWT. Los clientes (usuarios finales) interactuarán con la API a través de una aplicación móvil. El sistema debe manejar un volumen de 1 500 solicitudes por segundo en hora pico. Se espera que la API sea idempotente en las operaciones de creación y actualización de cuentas, utilizando el número de cuenta como clave. En caso de fallo del servicio de autenticación, la API debe continuar operando sin interrupciones.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Diseño y desarrollo de una API REST en el dominio de banca y fintech |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 10 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del modelo de datos y autenticación

**Objetivo:** Definir el modelo de datos para las cuentas bancarias y configurar la autenticación JWT.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Identificar las propiedades esenciales de una cuenta bancaria (número de cuenta, saldo, tipo de cuenta, titular).
- Definir el modelo de datos utilizando SQLAlchemy.
- Configurar la autenticación JWT para proteger los endpoints de la API.

**Entregable:** Modelo de datos para cuentas bancarias y configuración de autenticación JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los posibles valores y restricciones para cada propiedad de la cuenta bancaria.
- Piensa en cómo proteger los endpoints de la API para garantizar la seguridad de los datos.

</details>

### Fase 2: Implementación de endpoints CRUD

**Objetivo:** Implementar los endpoints CRUD para la gestión de cuentas bancarias.

**Tiempo estimado:** 4 horas

**Instrucciones:**

- Implementar los endpoints para crear, leer, actualizar y eliminar cuentas bancarias.
- Asegurar que las operaciones de creación y actualización sean idempotentes utilizando el número de cuenta como clave.
- Manejar los posibles errores y casos límite del dominio (cuentas inexistentes, saldo insuficiente).

**Entregable:** Endpoints CRUD para la gestión de cuentas bancarias.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo hacer que las operaciones de creación y actualización sean idempotentes.
- Considera los posibles errores y casos límite que podrían ocurrir en el dominio de las cuentas bancarias.

</details>

### Fase 3: Manejo de fallos y alta disponibilidad

**Objetivo:** Implementar mecanismos para manejar fallos y garantizar la alta disponibilidad de la API.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Implementar un mecanismo para continuar operando en caso de fallo del servicio de autenticación.
- Asegurar que la API pueda manejar un volumen de 1 500 solicitudes por segundo en hora pico.
- Considerar estrategias para mejorar la disponibilidad y resiliencia de la API.

**Entregable:** Mecanismos para manejar fallos y garantizar la alta disponibilidad de la API.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo podrías continuar operando en caso de fallo del servicio de autenticación.
- Considera estrategias para mejorar la disponibilidad y resiliencia de la API.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una cuenta bancaria y cuáles son sus propiedades esenciales?
- **paraQueSirve**: ¿Para qué sirve la autenticación JWT en una API REST?
- **comoSeUsa**: ¿Cómo se usa el modelo de datos de SQLAlchemy para definir una cuenta bancaria?
- **erroresComunes**: ¿Cuáles son los errores comunes que podrían ocurrir al gestionar cuentas bancarias a través de una API REST?
- **queDecisionesImplica**: ¿Qué decisiones implica implementar un mecanismo para continuar operando en caso de fallo del servicio de autenticación?

## Criterios de Evaluacion

- Definición del modelo de datos para cuentas bancarias.
- Configuración de autenticación JWT.
- Implementación de endpoints CRUD idempotentes.
- Manejo de errores y casos límite del dominio.
- Implementación de mecanismos para manejar fallos y garantizar la alta disponibilidad.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
