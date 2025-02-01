// Compilar:
// g++ -fopenmp openmp_sum.cpp -o openmp_sum

#include <iostream>
#include <omp.h>

int main() {
    long n = 100000000;     // Tamaño del bucle (100 millones)
    double sum = 0.0;

    // Tomar el tiempo de inicio
    double start = omp_get_wtime();

    // Comentar la línea 15 para deshabilitar openMP
    #pragma omp parallel for reduction(+:sum)
    for (long i = 0; i < n; i++) {
        sum += i;  // acumulamos la suma de i
    }

    // Tomar el tiempo de fin
    double end = omp_get_wtime();

    // Imprimir el resultado y el tiempo
    std::cout << "Resultado con OpenMP: " << sum << std::endl;
    std::cout << "Tiempo transcurrido: " << (end - start) << " segundos" << std::endl;

    return 0;
}
