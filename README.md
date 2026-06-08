# ejecicio-clase-10
Punto 1-
Una de las criticas principales a los patrones de diseño en programación es que los programadores principiantes intentan usarlos y meterlos a la fuerza. Dando como resultado algo mas complejo que en muchos casos se puede resolver con un simple if/else.
Otro caso de critica a su uso es el uso estricto de ciertos patrones fragmenta el código de una manera absurda. Para resolver una tarea sencilla, terminas creando una interfaz, una clase abstracta, tres implementaciones concretas y una fábrica.

un ejemplo de  critica es el uso de Singleton para una clase que podría instanciarse normalmente genera dependencia global y dificulta las pruebas. Cuando una aplicación depende de una única instancia global, muchas partes del sistema quedan atadas a ella. Si esa instancia falla o hay que cambiarla para realizar pruebas, todo se complica.

Punto 3-
**Problea 1: Grupo de WhatsApp**
Cuando alguien envía un mensaje en un grupo de WhatsApp, todos los integrantes reciben una notificación automáticamente.
Lo podemo resolver usando el patron de diseño Obvserver.
¿Por que? Porque existe un emisor (el grupo) y varios receptores (los miembros). Cada vez que ocurre un cambio (nuevo mensaje), todos los observadores son notificados sin que el emisor tenga que avisar a cada uno individualmente.

**Problema 2: compra en una tienda online**
Al realizar una compra, el cliente puede elegir entre distintos métodos de pago:

Tarjeta de crédito.
Tarjeta de débito.
Transferencia bancaria.
Mercado Pago.

Este problema se puede resolver usando Strategy.
Porque el sistema necesita diferentes formas de realizar la misma tarea (pagar). Cada método de pago representa una estrategia diferente y se puede cambiar sin modificar el resto del sistema

**Problema 3: Aplicación de delivery**

Cuando una persona hace un pedido en una aplicación de comida, solo presiona un botón para confirmar la compra.

Sin embargo, internamente el sistema:

Verifica el stock.
Procesa el pago.
Genera la orden.
Asigna un repartidor.
Envía notificaciones

lo podemos resolver usando Facade.
Lo usamos para que el usuario interactúa con una interfaz simple mientras que la fachada oculta toda la complejidad de los procesos internos.

Punto 4-
Nombre en ingles: Buider
Nombre alternativo: Constructor
Descripcion: Permite crear objetos complejos paso a paso.

Nombre en ingles: Prototype
Nombre alternativo: Prototipo
Descripcion: Crea nuevos objetos copiando uno existente

Nombre en ingles: Mediator
Nombre alternativo: Mediador
Descripcion: Centraliza la comunicación entre varios objetos.

Punto 5-
Los antipatrones son soluciones de diseño o programación que parecen resolver un problema de manera rápida o sencilla, pero que a largo plazo generan dificultades en el mantenimiento, la escalabilidad y la calidad del software.

Mientras que los patrones de diseño representan buenas prácticas comprobadas, los antipatrones representan errores frecuentes que los desarrolladores suelen cometer. Conocerlos permite identificar problemas en el código y evitar que se repitan en futuros proyectos.

Algunos ejemplos de esto son:
**God Object:**
Este antipatrón aparece cuando una única clase concentra demasiadas responsabilidades y controla gran parte del funcionamiento de la aplicación.
Un ejemplo de uso de este antipatron es en un sistema de gestión de una biblioteca existe una clase llamada Biblioteca que:
Administra usuarios.
Gestiona préstamos.
Registra devoluciones.
Calcula multas.
Genera reportes.
Controla el inventario de libros.

Aqui el problema esta en que al contener tantas responsabilidades, la clase se vuelve muy grande y compleja. Cualquier modificación puede afectar otras funcionalidades y aumentar la probabilidad de errores. Esto dara como consecuencia un codigo dificil de entender, mayor dificultad para realizar pruebas, el manteniminto sera costoso.

**Golden Hammer**
Ocurre cuando un desarrollador intenta resolver todos los problemas utilizando siempre la misma herramienta o tecnología.
Un ejemplo de este antipatron puede ser cuandfo un programador domina una determinada base de datos y decide utilizarla en todos sus proyectos, incluso cuando existen alternativas más adecuadas para ciertas necesidades.

Aqui EL problema esta en que cada problema tiene características diferentes y puede requerir soluciones distintas. Como consecuencia habra una perdida de rendimiento, sistemas menos eficientes y una mayor complejidad necesaria. 



