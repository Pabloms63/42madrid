# Codexion
*Este proyecto ha sido creado como parte del currículo de 42 por pmarcos-.*

## Descripción
Simulador de concurrencia donde múltiples threads (programadores) compiten por recursos 
limitados (dongles USB) usando mutexes POSIX y sincronización. Implementa dos políticas 
de planificación: FIFO y EDF (Earliest Deadline First).

Los programadores se sientan en círculo, cada uno necesita tomar dos dongles (izquierdo y derecho) 
simultáneamente para compilar. La simulación termina cuando todos han compilado el número 
requerido de veces o cuando alguien se agota por no compilar a tiempo.

## Instrucciones
```bash
make              # Compilar el proyecto
./codexion 4 400 200 100 50 10 50 fifo   # 4 coders, FIFO scheduler
./codexion 4 400 200 100 50 10 50 edf    # 4 coders, EDF scheduler
```

**Argumentos:**
- `number_of_coders`: Número de programadores (dongles)
- `time_to_burnout`: Milisegundos hasta agotamiento si no compila (ms)
- `time_to_compile`: Tiempo de compilación (ms)
- `time_to_debug`: Tiempo de debugging (ms)
- `time_to_refactor`: Tiempo de refactorización (ms)
- `number_of_compiles_required`: Número de compilaciones por completar
- `dongle_cooldown`: Enfriamiento de dongles tras liberarse (ms)
- `scheduler`: Política de arbitraje (`fifo` o `edf`)

## Blocking cases handled

### 1. **Deadlock Prevention (Circular Wait Avoidance)**
   - **Problema**: Dos threads esperando mutuamente por recursos puede causar deadlock
   - **Solución**: Los coders pares toman RIGHT primero, los impares LEFT primero
   - Esto asegura un orden consistente de adquisición, evitando esperas circulares

### 2. **Starvation Prevention with FIFO**
   - **Problema**: Algunos threads nunca acceden a recursos si otros los monopolizan
   - **Solución**: FIFO scheduler respeta orden estricto de llegada de solicitudes
   - Cada dongle mantiene una cola: primer llegado, primer servido

### 3. **Deadline Miss Prevention with EDF**
   - **Problema**: Algunos coders se agotan (burnout) si esperan demasiado
   - **Solución**: EDF (Earliest Deadline First) sirve primero al coder con deadline más próximo
   - Deadline = last_compile_start + time_to_burnout
   - Prioriza a coders en riesgo de agotamiento

### 4. **Cooldown Management**
   - **Problema**: Reuso inmediato de dongles puede causar race conditions
   - **Solución**: Cada dongle tiene período de enfriamiento tras liberarse
   - No puede volver a tomarse hasta que `get_time_ms() >= cooldown_until`

### 5. **Burnout Detection (Monitor Thread)**
   - **Problema**: Necesitamos detectar agotamiento rápido (< 10ms de tolerancia)
   - **Solución**: Thread monitor separado revisa cada coder cada 1ms
   - Verifica: `get_time_ms() - last_compile > time_to_burnout`

### 6. **Race Condition Prevention in Logging**
   - **Problema**: Múltiples threads escribiendo a stdout simultáneamente causa mezcla de mensajes
   - **Solución**: Mutex `log_mutex` protege todas las llamadas a `printf()`
   - Garantiza atomicidad: un mensaje por línea

### 7. **Compiler Coffman Conditions Avoidance**
Verificamos las 4 condiciones de Coffman y cómo las evitamos:
   - **Mutual Exclusion**: ✓ Mutex protege cada dongle
   - **Hold and Wait**: ✓ Circular order prevents waiting while holding
   - **No Preemption**: Permitimos (liberar y reintentar si imposible)
   - **Circular Wait**: ✓ Orden fijo de adquisición evita ciclos

## Thread synchronization mechanisms

### Primitives Used

1. **pthread_mutex_t** (uno por dongle + 2 globales)
   - `dongle->mutex`: Protege estado de disponibilidad y cooldown
   - `data->stop_mutex`: Protege flag de parada de simulación
   - `data->log_mutex`: Serializa salida a stdout

2. **pthread_cond_t** (implícito en cola)
   - Los dongles mantienen cola `waitlist` de requests
   - En FIFO: cola simple (mutex suficiente)
   - En EDF: cola ordenada por deadline

### Key Synchronization Patterns

#### Pattern 1: Acquiring Dongle (FIFO)
```c
pthread_mutex_lock(&dongle->mutex);
// Check cooldown
if (get_time_ms() < dongle->cooldown_until) {
    pthread_mutex_unlock(&dongle->mutex);
    return 0;  // Not ready yet
}
return 1;  // Keep mutex locked, coder now owns dongle
```

#### Pattern 2: Acquiring Dongle (EDF)
```c
pthread_mutex_lock(&dongle->mutex);
// Add to priority queue if not already there
add_to_queue_edf(dongle, coder_id, deadline);
// Check if we're first in queue AND cooldown passed
if (dongle->waitlist.head->coder_id == coder_id 
    && get_time_ms() >= dongle->cooldown_until) {
    dequeue_request(&dongle->waitlist);
    return 1;  // Keep mutex locked
}
pthread_mutex_unlock(&dongle->mutex);
return 0;
```

#### Pattern 3: Releasing Dongle
```c
dongle->cooldown_until = get_time_ms() + cooldown_ms;
pthread_mutex_unlock(&dongle->mutex);  // Release both mutexes
```

#### Pattern 4: Checking Burnout (Monitor)
```c
pthread_mutex_lock(&stop_mutex);
for each coder:
    if (get_time_ms() - coder->last_compile > time_to_burnout) {
        stop = 1;
        log "burned out"
    }
pthread_mutex_unlock(&stop_mutex);
```

### Race Condition Prevention

1. **Dongle State Race**: Mutex ensures only one coder can check/modify dongle
2. **Cooldown Race**: Cooldown_until checked INSIDE mutex before returning
3. **Last Compile Race**: Updated right before compilation begins
4. **Stop Flag Race**: Protected by `stop_mutex`, checked before critical operations
5. **Log Race**: Protected by `log_mutex`, ensures atomic printf

### Thread-Safe Communication Pattern

```
Coder Thread          Dongle         Monitor Thread
    |                  |                    |
    |-- acquire ------>|                    |
    |                  |                    |
    |<---- owned ------|                    |
    |                  |                    |
    |-- compile ------>|                    |
    |                  |                    |
    |-- release ------>|-- cooldown until  |
    |                  |    (protected)     |
    |                  |                    |
    |-- check last ---->|<--- check timeout |
    |    compile        |                    |
    |                  |                    |
```

## Recursos

- [POSIX Threads Reference](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [Dinning Philosophers Problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem)
- [Mutex and Condition Variables](https://linux.die.net/man/7/pthreads)
- [Earliest Deadline First Scheduling](https://en.wikipedia.org/wiki/Earliest_deadline_first)

### Uso de la IA en este proyecto
- **Parser & Utility Functions**: AI helped with structure design
- **Queue Implementation**: AI provided priority queue logic for EDF
- **Synchronization Patterns**: Verified against POSIX standards
- **All code reviewed and understood**: 100% comprehension before integration