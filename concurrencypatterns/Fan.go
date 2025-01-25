// Arreglo de Datos: data := []int{5, 2, 7, 3, 10} es el conjunto de “tareas” a procesar.
//
// Channels:
//  - tasks: canal para enviar los ítems a procesar.
//  - results: canal para recibir los resultados.

// fan-out:
//  - Se crean workerCount goroutines (3 en el ejemplo), cada una ejecuta la función worker().
//  - En worker(), se lee de tasks hasta que esté vacío o cerrado, se llama a process(item), y se escribe el resultado en results.

// fan-in:
//  - En el main(), tras lanzar los workers, cargamos todos los valores de data en tasks y luego cerramos el canal.
//  - Con wg.Wait() esperamos a que todos los workers terminen, cerrando results para indicar que no habrá más datos.
//  - Finalmente, recogemos todo de results en un bucle y acumulamos en sum.

// Resultado:
//  - Cada ítem en data es procesado por alguno de los workers.
//  - Se muestra la suma de todos los valores procesados (p. ej., 2*5 + 2*2 + 2*7 + 2*3 + 2*10 = 54).

// Recomendado: Estudiar goroutines
// https://leangaurav.medium.com/common-mistakes-when-using-golangs-sync-waitgroup-88188556ca54

package main

import (
	"fmt"
	"sync"
	"time"
)

// process simula una operación de cómputo en cada elemento
func process(item int) int {
	time.Sleep(50 * time.Millisecond) // simula tiempo de trabajo
	return item * 2
}

// worker recibe tareas desde tasks y envía los resultados a results
func worker(tasks <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for t := range tasks {
		out := process(t)
		results <- out
	}
}

func main() {
	data := []int{5, 2, 7, 3, 10}

	// fan-out: enviamos las tareas a un canal
	tasks := make(chan int, len(data))
	// fan-in: recogemos los resultados en otro canal
	results := make(chan int, len(data))

	// Definimos cuántos "workers" vamos a lanzar
	const workerCount = 3
	var wg sync.WaitGroup

	// Lanzar múltiples goroutines (fan-out) para procesar tareas
	for i := 0; i < workerCount; i++ {
		wg.Add(1)
		go worker(tasks, results, &wg)
	}

	// Enviar las tareas al canal
	for _, val := range data {
		tasks <- val
	}
	close(tasks)

	// Cuando las goroutines finalicen, cerramos el canal de resultados
	go func() {
		wg.Wait()
		close(results)
	}()

	// fan-in: recopilamos los resultados en un único punto
	var sum int
	for r := range results {
		sum += r
	}

	fmt.Println("Resultado fan-out/fan-in en Go:", sum)
}
