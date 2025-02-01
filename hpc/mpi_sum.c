// Instalar compilador para MPI, en Unix/Ubuntu por ejemplo:
// $ sudo apt install mpich

// Compilar:
// $ mpicc mpi_sum.c -o mpi_sum

// Ejecutar con parametro de número de procesos:
// $ mpirun -np 4 ./mpi_sum

// Detalles de implementación:
/*
   - MPI_Comm_size: indica cuántos procesos hay en total (size).
   - MPI_Comm_rank: asigna un índice (rank) a cada proceso.
   - local_val = rank * 10;: cada proceso tiene un valor distinto.
   - MPI_Reduce: combina esos valores en global_sum usando la operación MPI_SUM.
   - Solo el proceso rank=0 imprime el resultado.
*/
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int size, rank;
    MPI_Comm_size(MPI_COMM_WORLD, &size); // tamaño del communicator
    MPI_Comm_rank(MPI_COMM_WORLD, &rank); // identificador de proceso

    // valor local basado en el rank
    int local_val = rank * 10;
    int global_sum = 0;

    // Reducir todos los local_val en global_sum en el proceso root (0)
    MPI_Reduce(&local_val, &global_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if(rank == 0){
        printf("Suma global = %d\n", global_sum);
    }

    MPI_Finalize();
    return 0;
}
