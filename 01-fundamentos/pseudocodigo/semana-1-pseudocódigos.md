\# SEMANA 1: PSEUDOCÓDIGOS BÁSICOS



\## Ejercicio 1: Calcular años hasta jubilación



ALGORITMO: Calcular años hasta jubilación



ENTRADA: edad\_actual (número)

SALIDA: años\_restantes (número)



INICIO

&#x20; LEER edad\_actual

&#x20; 

&#x20; jubilacion = 65

&#x20; años\_restantes = jubilacion - edad\_actual

&#x20; 

&#x20; SI años\_restantes > 0:

&#x20;   MOSTRAR "Te faltan " + años\_restantes + " años para jubilarte"

&#x20; SI años\_restantes == 0:

&#x20;   MOSTRAR "¡Ya alcanzaste la edad de jubilación!"

&#x20; SI años\_restantes < 0:

&#x20;   MOSTRAR "¡Pasaste la edad de jubilación hace " + (años\_restantes \* -1) + " años!"

FIN



\---



\## Ejercicio 2: Encontrar el número más grande de una lista



ALGORITMO: Encontrar número más grande



ENTRADA: lista\_numeros (lista de números)

SALIDA: mayor (número)



INICIO

&#x20; LEER lista\_numeros

&#x20; 

&#x20; mayor = primer\_elemento(lista\_numeros)

&#x20; 

&#x20; PARA CADA numero EN lista\_numeros:

&#x20;   SI numero > mayor:

&#x20;     mayor = numero

&#x20; 

&#x20; MOSTRAR "El número más grande es: " + mayor

FIN



\---



\## Ejercicio 3: Verificar si un número es PAR o IMPAR



ALGORITMO: Verificar si número es par o impar



ENTRADA: numero (número entero)

SALIDA: resultado (texto: "par" o "impar")



INICIO

&#x20; LEER numero

&#x20; 

&#x20; SI numero % 2 == 0:

&#x20;   MOSTRAR numero + " es PAR"

&#x20; SI NO:

&#x20;   MOSTRAR numero + " es IMPAR"

FIN



EXPLICACIÓN:

\- El operador % (módulo) retorna el RESTO de la división

\- Si numero % 2 == 0, significa que NO hay resto, por lo tanto es PAR

\- Si numero % 2 == 1, hay resto, por lo tanto es IMPAR



\---



\## Ejercicio 4: Validar si un email tiene formato correcto



ALGORITMO: Validar formato de email



ENTRADA: email (texto)

SALIDA: válido (verdadero/falso)



INICIO

&#x20; LEER email

&#x20; 

&#x20; SI email CONTIENE "@":

&#x20;   SI email CONTIENE ".":

&#x20;     posicion\_arroba = POSICIÓN\_DE("@", email)

&#x20;     posicion\_punto = POSICIÓN\_DE(".", email)

&#x20;     

&#x20;     SI posicion\_arroba < posicion\_punto:

&#x20;       SI posicion\_arroba > 0:

&#x20;         SI posicion\_punto > posicion\_arroba + 1:

&#x20;           MOSTRAR "Email válido ✓"

&#x20;         SI NO:

&#x20;           MOSTRAR "Email inválido: falta dominio"

&#x20;       SI NO:

&#x20;         MOSTRAR "Email inválido: nada antes de @"

&#x20;     SI NO:

&#x20;       MOSTRAR "Email inválido: @ debe estar antes de ."

&#x20;   SI NO:

&#x20;     MOSTRAR "Email inválido: falta punto (.)"

&#x20; SI NO:

&#x20;   MOSTRAR "Email inválido: falta @"

FIN



EXPLICACIÓN:

\- Primero verificamos que exista @

\- Luego verificamos que exista un punto después del @

\- Verificamos que haya algo antes del @ y algo entre @ y .



\---



\## Ejercicio 5: Contar cuántas veces aparece una letra en una palabra



ALGORITMO: Contar apariciones de una letra



ENTRADA: palabra (texto), letra (carácter único)

SALIDA: contador (número)



INICIO

&#x20; LEER palabra

&#x20; LEER letra

&#x20; 

&#x20; contador = 0

&#x20; 

&#x20; PARA CADA caracter EN palabra:

&#x20;   SI caracter == letra:

&#x20;     contador = contador + 1

&#x20; 

&#x20; MOSTRAR "La letra '" + letra + "' aparece " + contador + " veces en '" + palabra + "'"

FIN



EJEMPLOS:

\- palabra = "programación", letra = "a" → resultado = 2

\- palabra = "JavaScript", letra = "a" → resultado = 1

\- palabra = "mississippi", letra = "s" → resultado = 4



EXPLICACIÓN:

\- Recorremos cada carácter de la palabra

\- Si el carácter coincide con la letra buscada, sumamos 1 al contador

\- Al final mostramos el total

