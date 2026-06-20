# Codexion
*Este proyecto ha sido creado como parte del currículo de 42 por pmarcos-.*

## Description
Simulador de concurrencia donde múltiples threads (programadores) compiten por recursos 
limitados (dongles USB) usando mutexes POSIX y sincronización. Implementa dos políticas 
de planificación: FIFO y EDF (Earliest Deadline First).

## Instructions
make
./codexion 4 400 200 100 50 10 50 fifo
./codexion 4 400 200 100 50 10 50 edf

## Blocking cases handled

- **Deadlock prevention**: Pares toman RIGHT primero, impares LEFT primero
- **Starvation prevention**: FIFO scheduler es justo (primer llegado, primer servido)
- **Cooldown management**: Dongles no reutilizables hasta cooldown_until
- **Burnout detection**: Monitor revisa cada 1ms

## Thread synchronization mechanisms

- **pthread_mutex_t**: Protege cada dongle
- **Cooldown loops**: Espera hasta cooldown_until
- **Monitor thread**: Detecta burnout

## Resources

- [POSIX Threads](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)
- [Dinning Philosophers](https://en.wikipedia.org/wiki/Dining_philosophers_problem)