#Breve descripción del sistema
Bienvenido/as. Este sistema pretende servir de inventario para el registro y consulta de equipos médicos instalados en un Hospital. Aquí se pueden registrar
equipos, referentes de cada sector donde se hayan instalados los mismos y proveedores con su información de contacto para recibir soporte.

#Instalar el proyecto
Para instalar el proyecto se deben seguir los siguientes pasos:
- descargar el repositorio al equipo local y abrirlo con la aplicación vscode.
- Una vez abierto, correr en la terminal de VSCODE el comando python manage.py runserver.
- A continuación, se mostrará la url generada localmente para acceder al proyecto.
- La url de inicio es: http://127.0.0.1:8000/index/
    
#Navegar dentro del proyecto
En el proyecto hay un botón Inicio (en el futuro, en una versión final, será el botón para iniciar sesión y poder cargar y consultar datos después de autenticar). Para volver siempre a la
página inicial, presione ese botón.
Luego verá 3 pestañas, cada una hace referencia a una parte del inventario.

#Cómo utilizar el sistema
- Si desea ver la lista de Referentesm presione en la pestaña referentes. Si desea cargar un nuevo referente, presione el botón CREAR REFERENTE, rellene los campos y presione CREAR REFERENTE. A continuación, será redirigido a la pestaña anterior, donde verá todos los referentes cargados.
- Los mismos pasos deben realizarse para Proveedores y Equipos.
- Como equipos es la parte más importante del proyecto y la que más campos va a llegar a tener, se creó un apartado de búsqueda para que sea más fácil ubicar un equipo en especial. Simplemente vaya a la pestaña Equipos rellene el casillero que verá allí y presiones Buscar por equipo. A continuación, se mostrarán todos los resultados para su búsqueda.
