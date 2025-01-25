# Observaciones y Comparación

## Lógica Común:
En todos los casos se procesa el mismo arreglo [5, 2, 7, 3, 10] en 2 “trabajadores” (workers) que suman a un recurso o estado compartido.

## Diferencias:
- Java (Hilos + Locks): necesitamos sincronizar acceso a total con synchronized.
- Elixir (Actores): cada trabajador envía mensajes y el actor mantiene un único estado.
- Haskell (STM): las actualizaciones son atómicas mediante transacciones.
- C++ (Lock-free): se usa compare_exchange_weak en bucles para lograr una operación CAS.

## Resultado:
En todos se espera una suma duplicada: sum([5,2,7,3,10]) * 2 = 54.

## Complejidad vs. Legibilidad:
- Java e Haskell ofrecen abstracciones más claras (locks, transacciones),
- Elixir (actor) simplifica la contención al delegar en un proceso maestro,
- C++ lock-free es muy rápido pero complejo de mantener y propenso a errores si no se domina la atomics API.
