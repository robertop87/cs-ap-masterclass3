// C++ (uso de std::atomic<int> y un bucle con Compare-And-Swap).

// std::atomic<int> total{0}; evita un lock tradicional.
// En worker, cada vez que se suma val, se usa compare_exchange_weak para actualizar total sin bloqueos.
// Si otro hilo modifica total en medio, compare_exchange_weak falla y repite el do-while.
// Resultado: Suma duplicada de [5, 2, 7, 3, 10].

#include <iostream>
#include <thread>
#include <atomic>
#include <vector>
#include <chrono>

std::atomic<int> total{0};

void worker(const std::vector<int>& tasks) {
    for(int val : tasks) {
        // Simular trabajo
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
        int oldVal = total.load(std::memory_order_relaxed);
        int newVal;
        do {
            newVal = oldVal + val;
        } while(!total.compare_exchange_weak(oldVal, newVal,
                  std::memory_order_release,
                  std::memory_order_relaxed));
    }
}

int main() {
    std::vector<int> tasks = {5, 2, 7, 3, 10};

    // Lanzar 2 hilos
    std::thread t1(worker, std::ref(tasks));
    std::thread t2(worker, std::ref(tasks));

    t1.join();
    t2.join();

    std::cout << "Resultado final (C++ lock-free): " << total.load() << "\n";
    return 0;
}
