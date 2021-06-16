# ParcialHerramientasComputacionales
_En este repositorio se encuentra los archivos necesarios para la comprensión del parcial de Herramientas computacionales(documentación y solución)_

## Documentacion del problema

La solución refleja un tipo de sistema para un cajero, en el cual, se ira llenando la información requerida para generarle al final el total a pagar o factura.  En la primera parte, hay un pequeño menú que le permitirá al cajero acabar con el programa o proceder a registrar los artículos. Si se decide continuar con la facturación, se le pide al cliente su cedula y si es estudiante o profesor. Luego, se ingresa el código del producto, las unidades de este, y el precio unitario, para posteriormente realizar un procedimiento en donde se le saque un porcentaje de descuento a cada artículo. Si es estudiante el 50% y si es profesor el 20%.  Una vez calculado el valor con descuento ((precio * und )* 0.5), se procederá a guardar tanto este valor como el código del producto en una lista, la cual será guardada posteriormente en otra lista llamada (CompraTotal). Quedando así como una especie de matriz o lista de listas. Seguido a esto, se pregunta si se registraran mas productos, si la respuesta el sí, se volverá a ejecutar el ciclo para registrar los productos los cuales irán quedando en la lista (CompraTotal). Cuando el usuario no tenga mas productos para registrar se procede a recorrer la lista (CompraTotal), de modo que le muestre al usuario cuanto debe pagar por cada articulo al igual que el código de este. En la última parte podrá visualizar el total de la factura. 

Para la implementacion en python puede verse en el archivo: **FinalHerramientas.py**.

### Los posibles errores y estrategias

Se muestra que tipo de errores pudimos haber cometido durante la codificación y cuales fueron nuestras estrategias para corregir estos errores dentro del programa.

Puede verse la información en el archivo: **Posibles errores y estrategias.docx**.
 
