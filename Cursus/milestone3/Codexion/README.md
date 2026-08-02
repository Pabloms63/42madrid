*Este proyecto ha sido creado como parte del currículo de 42 por pmarcos-.*

# Codexion

## Descripción
Codexion es una simulación de concurrencia en C: varias personas que programan
(coders) se sientan en un círculo y compiten por dongles USB compartidos para
compilar código. Cada persona necesita dos dongles (izquierdo y derecho) a la vez
para compilar, luego los libera y pasa a depurar y refactorizar. El objetivo es
que nadie se agote (burnout) por falta de acceso a los dongles, usando hilos
POSIX, mutexes y una cola de prioridad (heap) para arbitrar el acceso según el
scheduler elegido (`fifo` o `edf`).

## Instrucciones
```bash
make
./codexion number_of_coders time_to_burnout time_to_compile time_to_debug \
           time_to_refactor number_of_compiles_required dongle_cooldown scheduler
```

Ejemplo:
```bash
./codexion 4 400 200 100 5 2 50 fifo
./codexion 4 400 200 100 5 2 50 edf
```

**Argumentos:**
- `number_of_coders`: número de personas que programan (y de dongles)
- `time_to_burnout`: ms sin compilar antes de agotarse
- `time_to_compile`: ms que dura la compilación
- `time_to_debug`: ms que dura la depuración
- `time_to_refactor`: ms que dura la refactorización
- `number_of_compiles_required`: compilaciones mínimas para terminar la simulación
- `dongle_cooldown`: ms de enfriamiento de un dongle tras liberarse
- `scheduler`: política de arbitraje, `fifo` o `edf`

## Casos de error gestionados
- **Deadlock**: orden de adquisición alternado (los coders pares toman
  right→left, los impares left→right) para romper la espera circular.
- **Condiciones de Coffman**: exclusión mutua mediante un mutex por dongle; no
  hay espera indefinida reteniendo un recurso (si falla el segundo dongle, se
  libera el primero); el orden fijo de adquisición evita el ciclo de espera.
- **Starvation (inanición)**: con `fifo` se respeta estrictamente el orden de
  llegada; con `edf` se prioriza a quien tiene el deadline de burnout más
  próximo.
- **Cooldown**: un dongle liberado no puede reasignarse hasta que pase
  `dongle_cooldown`, comprobado dentro de la sección crítica del mutex.
- **Detección de agotamiento**: un hilo `monitor` separado revisa cada coder
  periódicamente y registra el burnout dentro de los 10 ms posteriores al
  momento real en que ocurre.
- **Serialización del log**: un mutex (`log_mutex`) protege toda salida por
  `printf`, evitando que se mezclen dos mensajes en una misma línea (race
  condition en la salida).

## Mecanismos de sincronización de hilos
- `pthread_mutex_t` por dongle: protege su disponibilidad, el cooldown y la
  cola de espera (heap FIFO/EDF).
- `pthread_mutex_t` por coder: protege `last_compile` y `compile_count`,
  leídos tanto por el propio coder como por el monitor.
- `stop_mutex`: protege el flag global de parada de la simulación.
- `log_mutex`: serializa la escritura de logs.
- Cola de prioridad (min-heap) propia para ordenar las solicitudes de cada
  dongle por orden de llegada (fifo) o por deadline (edf), evitando race
  conditions al insertar o extraer solicitudes.
- La comunicación entre coders y el monitor es thread-safe porque nunca se
  accede a un dato compartido sin su mutex correspondiente; el monitor detiene
  la simulación mediante `stop_mutex`, y todos los hilos consultan ese flag de
  forma protegida antes de continuar con la siguiente fase.

## Recursos
- [Earliest Deadline First Scheduling](https://en.wikipedia.org/wiki/Earliest_deadline_first)
- [Video explicativo concurrencia - Problema filósofos](https://youtu.be/8KFvrgbuWxY?si=VUSUHFI3uT-nQQLJ)
- [POSIX Threads Reference](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [Dining Philosophers Problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
- [Binary heap](https://en.wikipedia.org/wiki/Binary_heap)

**Uso de IA**: se usó para debatir el diseño del arbitraje FIFO/EDF con heap y
para revisar la lógica de sincronización (mutex/cooldown). Todo el código fue
comprendido, probado y ajustado manualmente antes de integrarse.