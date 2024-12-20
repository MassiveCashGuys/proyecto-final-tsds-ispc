# Proyecto Final - TSDS - ISPC

---

## Primer Etapa:

**Proyecto Final del Módulo Programador del 1er año de Tecnicatura Superior en Desarrollo de Software ISPC.**

**Acceso rápido a Wiki:** [Wiki del Proyecto](https://github.com/MassiveCashGuys/proyecto-final-tsds-ispc/wiki)

Subimos por separado los archivos de las imágenes del modelo relacional y el modelo de clases para su mejor lectura.

---

## Segunda Etapa:

**Programación:** [Link a la Carpeta](https://github.com/MassiveCashGuys/proyecto-final-tsds-ispc/tree/back/documentaci%C3%B3n/Programacion)

**Base de Datos:** [Link a la Carpeta](https://github.com/MassiveCashGuys/proyecto-final-tsds-ispc/tree/back/documentaci%C3%B3n/BaseDeDatos)

**Competencias Comunicacionales II:** [Link a la Carpeta]()

---

## Propósito

Desarrollar una aplicación de demostración para ISPC Cba, un broker de bolsa registrado que actúa como intermediario entre los inversores y la Bolsa de Valores de Buenos Aires (MERVAL). La aplicación permitirá la simulación de transacciones de compra y venta de acciones, proporcionando una plataforma interactiva para facilitar la comprensión del mercado de valores y sus operaciones.

---

## Contexto

ISPC Cba, como broker autorizado, busca ofrecer una herramienta de simulación funcional para inversores potenciales (personas físicas, empresas o instituciones). Este proyecto se enmarca en el contexto de mejorar los servicios ofrecidos por ISPC Cba, proporcionando una plataforma que refleja las dinámicas del mercado de valores. La aplicación servirá como prototipo para que ISPC Cba utilice la herramienta para atraer y educar a nuevos inversores.

---

## Alcance

* Simulación de Transacciones: Permitir la compra y venta simulada de acciones en el MERVAL, con precios de referencia actualizados regularmente.
* Gestión de Portafolio: Funcionalidad para que los usuarios visualicen el desempeño de su portafolio de inversiones simulado, incluyendo valores actuales de sus acciones.
* Historial de Transacciones: Registro detallado de todas las transacciones simuladas (compra, venta) realizadas por el usuario, mostrando atributos como fecha, precio, cantidad, comisión, y tipo de acción.
* Análisis de Rendimiento: Proveer gráficos y estadísticas que reflejen el rendimiento histórico y actual del portafolio, calculando ganancias y pérdidas potenciales.
* Simulación de Comisiones y Costos: Incluir simulación de comisiones y costos asociados a cada transacción para que el usuario entienda los gastos relacionados con la compra y venta de acciones.
* Educación Financiera: Sección con materiales educativos sobre el funcionamiento del mercado de valores y consejos para invertir de manera informada.
* Evaluación de Riesgo: Herramientas y métricas para evaluar el riesgo asociado a diferentes transacciones.

## Autores

- **Marini Alan**  
  - DNI: 35785659  
  - Email: [aland.marini@gmail.com](mailto:aland.marini@gmail.com)  
  - Usuario de GitHub: [AlandMarini](https://github.com/AlandMarini)

- **Martín Julio**  
  - DNI: 30657441  
  - Email: [JulioMartin447@gmail.com](mailto:JulioMartin447@gmail.com)  
  - Usuario de GitHub: [JulioMartin12](https://github.com/JulioMartin12)

- **Olmos Gustavo**  
  - DNI: 29253219  
  - Email: [programacionwebolmos@gmail.com](mailto:programacionwebolmos@gmail.com)  
  - Usuario de GitHub: [gusta37](https://github.com/gusta37)

- **Portillo Marcelo Martín**  
  - DNI: 27644034  
  - Email: [mportillo79@gmail.com](mailto:mportillo79@gmail.com)  
  - Usuario de GitHub: [mapolab](https://github.com/mapolab)

- **Quiroga Lucas Javier**  
  - DNI: 39215587  
  - Email: [quiroga.lucasj@gmail.com](mailto:quiroga.lucasj@gmail.com)  
  - Usuario de GitHub: [LucasJQ13](https://github.com/LucasJQ13)

---

## Instrucciones de Instalación-Entorno

1. **Crear un entorno virtual:**  
   Dentro del proyecto en la raíz, desde la terminal ejecutar el siguiente comando:  
   `python -m venv entorno`

2. **Activar el entorno virtual:**  
   Desde la terminal ejecutar el siguiente comando:  
   `entorno\Scripts\activate`

3. **Instalar todas las dependencias:**  
   Con el entorno activado, ejecuta el siguiente comando para instalar las dependencias:  
   `pip install -r requirements.txt`

4. **Desactivar el entorno virtual:**  
   Ejecutar el siguiente comando:  
   `deactivate`

5. **Crear archivo `.env`:**  
   Para sus variables de entorno y resguardar las credenciales. 
   globales:  
   USER=" "
   PASSWORD=" "
   HOST=" " 
   DATABASE=" " 
   PORT=" "
