# 🎓 Ejemplos de Uso: HelixIncident

¡Hola! Bienvenido al campo de entrenamiento de **HelixIncident**.

Si estás aquí, es porque quieres ver a este módulo en acción. Su misión, inspirada en *"The Gunslinger"*, es clara: **Automatiza respuesta a incidentes**.

Aquí encontrarás ejemplos prácticos para entender cómo integrarlo en tus sistemas sin dolor de cabeza.

## 📂 Contenido

- `basic_usage.py`: Un script listo para ejecutar que demuestra el flujo básico de trabajo.

## 🚀 Cómo ejecutar el ejemplo

Es muy sencillo. Desde la raíz del proyecto (o desde este directorio), ejecuta:

```bash
python basic_usage.py
```

## 🧠 ¿Qué está pasando en el código?

El script `basic_usage.py` sigue un flujo lógico de 4 pasos que verás en casi todos nuestros módulos:

1.  **Invocación**: Importamos e instanciamos la clase principal `HelixIncident`. Es como sacar al módulo de su sistema.
2.  **Preparación**: (Opcional) Usamos `.validate()` para asegurarnos de que los datos de entrada (si los hay) son seguros y correctos.
3.  **Acción**: Llamamos a `.analyze()` (o métodos específicos como `.scan()`, `.encrypt()`). Aquí es donde ocurre la magia de seguridad.
4.  **Reporte**: Recibimos un objeto `AnalysisResult` estructurado. No más adivinar qué pasó; el módulo te dice exactamente si hubo éxito, advertencia o error.

## 💡 Tips Pro

*   **Configuración**: La mayoría de estos módulos aceptan un diccionario `config` al inicializarse. ¡No tengas miedo de personalizarlo! Revisa el archivo `USAGE.md` en el directorio padre para ver las opciones.
*   **Integración**: Este código está diseñado para ser copiado y pegado (con ligeros ajustes) en tus pipelines de CI/CD o scripts de automatización.

---
*"La seguridad no es un destino, es un viaje constante... y es mejor hacerlo acompañado de un buen módulo."*