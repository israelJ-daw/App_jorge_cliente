para poder probar las validaciones: si pones "pepe" en nombre en categorias te aparece una categoria, y si quieres otra pones "nou"

validadcion en propiedad: para que te salgan todas puedes poner "propi" y ya si quieres que te salga 1 pues pones su titulo, por ejemplo "propiedad 1" y solo te saldra la propiedad 1

validaciones para servicio extra: debes marcar la casilla disponible porque todas las que tengo estan disponible, si no, no saldra nada, puedes poner en nombre "desayuno" y te saldra desayuno en cama, o "camas" y te saldra camas dobles o puedes poner "cena" y te saldra cena 

Respuestas preguntas:

1. Por cada petición que hemos hecho, se ha incluido siempre lo siguiente:http://127.0.0.1:8000/api/v1/libros/, que pasaría si en un futuro, la versión cambiar.¿Deberíamos cambiarlo en todos los sitios de la aplicación?¿Cómo podríamos mejorarlo?

Respuesta: Si, en el futuro se actualiza la versión de la API, por ejemplo, a v2, tendriamos que modificar esta url en todos los lugares donde se realice una solicitud

podemos mejorar centralizando la URL base en una variable, para que si cambia la versión, solo sea necesario actualizarla en un unico lugar.


2. Para la respuesta siempre incluimos la misma línea:response.json(). ¿Qué pasaría si en el día de mañana cambia el formato en una nueva versión, y en vez de json es xml?¿Debemos volver a cambiar xmlen todos los sitios esa línea? 

Respuesta: Si cambiamos el formato a xml, response.json() no funcionaría, ya que está diseñado para json, tendriamos que usar response.text()

Si, si no centralizamos la logica de manejo de respuestas, tendriamos que cambiar response.json() en todos los lugares a response.text()    

3. ¿Siempre debemos tratar todos los errores en cada una de las peticiones?

REspuesta:

si ,es muy importante gestionar los errores en cada solicitud para prevenir fallos inesperados, asi mejoreamos la experiencia del usuario y aumentamos la seguridad

