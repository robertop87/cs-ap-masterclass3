// Ejemplo usando Thread. Memoria compartida

// Se define una clase SharedCounter con un total compartido.
// Se usan métodos synchronized para bloquear el acceso concurrente.
// Se lanza 2 hilos (cada uno procesa el array tasks, sumando los mismos valores).
// Resultado esperado: El total será la suma duplicada de [5, 2, 7, 3, 10] (2 veces).

public class SharedCounter {
    private int total = 0;

    public synchronized void add(int value) {
        total += value;
    }

    public synchronized int getTotal() {
        return total;
    }

    public static void main(String[] args) throws InterruptedException {
        SharedCounter counter = new SharedCounter();
        int[] tasks = {5, 2, 7, 3, 10};

        Runnable worker = () -> {
            for (int val : tasks) {
                // Simular trabajo (p.ej. dormir un poco)
                try { Thread.sleep(50); } catch (InterruptedException e) {}
                counter.add(val);
            }
        };

        // Crear 2 hilos
        Thread t1 = new Thread(worker);
        Thread t2 = new Thread(worker);

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Resultado final (Java, hilos+locks): " + counter.getTotal());
    }
}
