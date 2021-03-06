# Windows 10 App Essentials #

* Autores: Joseph Lee, Derek Riemer y otros usuarios de Windows 10
* Descargar [versión estable][1]
* Descargar [versión de desarrollo][2]

Este complemento es una colección de app modules para varias aplicaciones de
Windows 10, así como correcciones para ciertos controles de windows 10.

Se incluyen Los siguientes app modules o el apoyo para módulos para algunas
aplicaciones (consulta cada sección para la aplicación para detalles sobre
qué se incluye):

* Reloj y alarmas.
* Calendario
* Calculadora (modern).
* Cortana
* Groove Music
* Correo
* Mapas
* Microsoft Edge
* Settings (system settings, Windows+I)
* Skype (universal app)
* Tienda
* El Tiempo
* Módulos misceláneos para controles tales como los mosaicos del Menú
  Inicio.

Note: this add-on requires Windows 10 Version 1511 (build 10586) or later
and NVDA 2016.4 or later. For best results, use the add-on with latest
stable build (build 14393) and latest stable version of NVDA. Also, after
changing update settings for the add-on, be sure to save NVDA settings.

## General

* En menús de contexto para los mosaicos del Menú Inicio, los submenús ahora
  se reconocen apropiadamente.
* Al minimizar windows (Windows+M), ya no se anuncia "panel" ­(­perceptible
  si se utilizan compilaciones Insider Preview).
* Ahora se reconocen ciertos diálogos como diálogos apropiadamente. Esto
  incluye el diálogo Insider Preview (aplicación de configuración) y el
  diálogo de nuevo estilo del UAC en la compilación 14328 y posteriores para
  NvDA 2016.2.1 o anteriores.
* La apariencia o cierre de sugerencias para ciertos campos de búsqueda (en
  particular la app Opciones) se anuncian a través de sonidos y/o de
  braille. Esto también incluye el cuadro de búsqueda del menú Inicio.
* NVDA puede anunciar cuenta de sugerencias cuando se realiza una búsqueda
  en la mayoría de casos. Esta opción se controla por "Anunciar información
  de posición del objeto" en el diálogo Presentación de Objetos.
* En ciertos menús de contexto (tales como en Edge), la información de
  posición (ej.: 1 de 2) ya no se anuncia.
* Se reconocen los siguientes eventos UIA: Controller para, live region
  cambiada (manejada por  evento de cambio de nombre).
* Engadida a capacidade de procurar actualizacións do complemento
  (automática ou manual) a través do novo diálogo Windows 10 App Essentials
  que se atopa no menú Preferencias do NVDA. Por defecto, procuraranse as
  actualizacións para as versións estable e de desenvolvemento
  automáticamente semanal ou diáriamente, respectivamente.
* Capacidad para seguir eventos que lleguen desde aplicaciones Universal
  Windows Platform (UWP) si NVDA se está ejecutando con el registro de
  depuración habilitado (2017.1 o posterior).

## Alarmas y reloj

* Ahora se anuncian los valores del selector de hora. Esto también afecta al
  control utilizado para seleccionar cuándo reiniciar para finalizar la
  instalación de las actualizaciones de Windows.

## Calculadora

* Cuando se pulse INTRO, NVDA anuncia los resultados del cálculo.

## calendario

* NVDA ya no anuncia "editar" o "sólo lectura" en el cuerpo del mensaje y
  otros campos.

## Cortana

* Las respuestas textuales de Cortana se anuncian en la mayoría de las
  situaciones (si no se reabre el menú Inicio y  se trata de buscar de
  nuevo).
* NVDA se silenciará cuando hables a Cortana a través de la voz.
* NVDA ahora anunciará confirmación de recuerdo después de configurarla.

## Groove Music

* Ahora se detecta la aparición de sugerencias cuando se detecta búsqueda de
  pistas .

## Correo

* Cando se revisan elementos na listaxe de mensaxes, agora podes usar ordes
  de navegación de táboas para revisar as cabeceiras de mensaxe.

## Mapas

* NVDA reproduce pitidos de localización para lugares en el mapa.
* Cuando se utiliza la vista lateral de la calle y si la opción "usar
  teclado" está habilitada, NVDA anunciará las direcciones de las calles
  según utilices las teclas de flechas para navegar por el mapa.

## Microsoft Edge

* Ahora se anuncian notificaciones tales como descargas de ficheros.
* In Creators Update, NVDA will no longer announce "WebRuntime Content View"
  when going to another site.

## Opciones

* Cierta información tal como el progreso de la Actualización de Windows
  ahora se anuncia automáticamente.
* Los valores de la barra de progreso y otra información ya no se anuncian
  dos veces.
* Si se toma un tiempo para buscar la configuración, NVDA anunciará
  "buscando" y el estado de los resultados de búsqueda tal como si una
  ocpión no se encontrara.
* Los grupos de opciones se reconocen cuando se utilice la navegación de
  objetos para navegar entre controles.
* Para algunos cuadros combinados, NVDA ya no fallará al reconocer etiquetas
  y/o al anunciar cambios de valores.

## Skype

* Al teclear el indicador de texto se anuncia sólo como cliente Skype para
  Escritorio.
* Retorno parcial de las órdenes Control+NVDA+fila de números para leer el
  historial de chats recientes y para mover el navegador de objetos a las
  entradas de chat como en Skype para Escritorio.
* Ahora puedes pulsar Alt+fila de números para localizar y mover a lista de
  contactos (1), conversaciones (2) y campo de edición de chat (3). Ten en
  cuenta que deben activarse esas pestañas para moverse a la parte decidida.
* Se anuncian las etiquetas de los cuadros combinados para la aplicación
  Skype preview liberada en Noviembre de 2016.
* NVDA ya no anuncia "Mensaje Skype" cuando se revisen mensajes para la
  mayoría de los casos.

## Tienda

* Después de buscar actualizaciones de aplicaciones, los nombres de las
  aplicaciones en la lista de aplicaciones etiquetadas se actualizan
  correctamente.
* Ahora se anuncia la aparición de sugerencias de búsqueda.
* Cuando se cargue contenido tal como aplicaciones y películas, NVDA
  anunciará el nombre del producto y el progreso de la descarga.

## El Tiempo

* Pestañas tales como "pronósticos" y "mapas" se reconocen como propias
  pestañas (parche de Derek Riemer).
* cuando se lea un pronóstico, utiliza las flechas izquierda y derecha para
  moverte entre elementos. Utiliza flechas arriba y abajo para leer los
  elementos individuales. Por ejemplo, pulsando la flecha derecha anunciaría
  "Lunes: 79 grados, parcialmente nublado, ..." pulsando flecha abajo dirá
  "lunes" entonces pulsándola de nuevo leerá el siguiente elemento (como la
  temperatura). Actualmente esto funciona para los pronósticos diarios y
  horarios.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=w10

[2]: https://addons.nvda-project.org/files/get.php?file=w10-dev
