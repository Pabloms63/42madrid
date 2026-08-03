*Este proyecto ha sido creado como parte del currículo de 42 por pmarcos-.*

# Codexion
## Descripción
Simulación de concurrencia donde varios programadores compiten por dongles USB
compartidos usando hilos y mutexes. Cada uno se sienta en círculo y necesita los dos
dongles de al lado (izquierda y derecha) para compilar. Hay dos formas de repartir los
dongles cuando hay cola: FIFO (por orden de llegada) o EDF (prioriza a quien está más
cerca de agotarse). La simulación acaba cuando todos han compilado las veces pedidas, o
en cuanto alguien se agota por no compilar a tiempo.

## Instrucciones
```bash
make
./codexion 4 1500 200 100 50 10 50 fifo   # 4 coders, con FIFO
./codexion 4 1500 200 100 50 10 50 edf    # 4 coders, con EDF
```
Los argumentos van en este orden: número de coders, tiempo hasta agotarse,
tiempo de compilar/depurar/refactorizar, compilaciones necesarias, enfriamiento del
dongle y el scheduler (`fifo` o `edf`). Todos son obligatorios y deben ser números
enteros positivos.

## Blocking cases handled

- **Interbloqueos**: si todos cogieran siempre "primero el dongle de la izquierda" se
  podría formar un círculo de espera sin fin. Para evitarlo, la mitad coge primero el
  de la derecha y la otra mitad el de la izquierda (según si el id es par o impar), así
  nunca se cierra el ciclo.

- **Reparto justo (FIFO/EDF)**: cada dongle tiene su propia cola. Al principio tenía un
  bug: el mutex se quedaba bloqueado mientras alguien compilaba, así que nadie más podía
  ni siquiera apuntarse a esperar — el orden real lo decidía el sistema operativo, no
  nuestra cola. Se arregló separando "quién tiene el dongle" (un flag) de "proteger la
  cola" (el mutex), para que todo el mundo pueda encolarse aunque el dongle esté en uso.

- **Enfriamiento (cooldown)**: al soltar un dongle, no se puede volver a coger hasta
  que pase el tiempo de enfriamiento. Se comprueba siempre bajo el mismo mutex que
  protege el resto del estado del dongle, así que no hay carreras raras ahí.

- **Detectar el agotamiento**: un hilo aparte (`monitor`) revisa cada poco tiempo si
  alguien lleva demasiado sin compilar, y para la simulación en cuanto lo detecta.

- **Que no se mezclen los logs**: todos los `printf` de estado pasan por el mismo mutex,
  así que nunca salen dos líneas mezcladas.

Nota: como cada dongle solo lo pueden pedir dos personas (sus vecinos), FIFO y EDF se
parecen bastante casi siempre — solo se nota la diferencia cuando esos dos vecinos
están esperando el mismo dongle exactamente a la vez.

## Thread synchronization mechanisms

- Un `mutex` por dongle, que protege si está libre, el enfriamiento y la cola de espera.
- Un `mutex` por coder, que protege cuándo compiló por última vez y cuántas veces lleva.
- Dos mutex globales: uno para parar la simulación y otro para que los logs no se mezclen.
- Una variable de condición (`pthread_cond_t`) por dongle: en vez de estar comprobando
  todo el rato si el dongle está libre (gastando CPU sin necesidad), el hilo se queda
  dormido ahí y se despierta solo cuando alguien suelta el dongle o cuando toca revisar
  el enfriamiento.

En resumen: nadie se queda con dos mutex a la vez, así que no hay forma de que se
bloqueen mutuamente esperándose el uno al otro.

## Recursos
- [Conceptos generales, explicación paradoja](https://youtu.be/8KFvrgbuWxY?si=N1pdHK99kO4jx6uX)
- [Info. y conceptos generales](https://www.youtube.com/watch?v=9Z-GcOI7MI4)
- [POSIX Threads Reference](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [Dining Philosophers Problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
- [Earliest Deadline First Scheduling](https://en.wikipedia.org/wiki/Earliest_deadline_first)

### Uso de la IA en este proyecto
Se usó IA para encontrar un bug de concurrencia real: la primera versión bloqueaba el
mutex del dongle mientras alguien compilaba, así que la cola FIFO/EDF nunca tenía más
de una persona esperando (el orden lo decidía el sistema operativo, no el scheduler).
También se usó para escribir un par de pruebas sueltas (no entregadas) que comprueban
que la cola reparte bien por FIFO y por EDF, y para revisar el resto del código
buscando fugas de memoria o carreras de datos. Todo el código se entendió y se probó
antes de dejarlo así.