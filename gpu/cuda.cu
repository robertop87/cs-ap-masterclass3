// Instalación NVIDIA toolkit: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
// Compilación:
// $ nvcc cuda_add.cu -o cuda_add

// Requiere hardware GPU NVIDIA
// Verificar en su sistema, ejemplo Ubuntu 22
// $ nvidia-detector

#include <iostream>
#include <cuda_runtime.h>

__global__ void addValue(int* arr, int val, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if(idx < n) {
        arr[idx] += val;
    }
}

int main() {
    int n = 5;
    int size = n * sizeof(int);
    int h_data[5] = {1, 2, 3, 4, 5};
    int *d_data;

    // Reservar memoria en la GPU
    cudaMalloc((void**)&d_data, size);
    // Copiar datos desde la CPU (host) a la GPU (device)
    cudaMemcpy(d_data, h_data, size, cudaMemcpyHostToDevice);

    // Lanzar kernel: 1 bloque, n hilos por bloque
    addValue<<<1, n>>>(d_data, 10, n);
    // Esperar a que la GPU termine
    cudaDeviceSynchronize();

    // Copiar resultados de la GPU al host
    cudaMemcpy(h_data, d_data, size, cudaMemcpyDeviceToHost);
    for(int i=0; i<n; i++){
        std::cout << "Pos " << i << " = " << h_data[i] << std::endl;
    }

    cudaFree(d_data);
    return 0;
}
