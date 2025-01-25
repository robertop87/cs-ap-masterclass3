#  Elixir (paradigma de actores, usando send y receive).

# SumActor maneja mensajes de dos tipos: {:add, val, sender} para sumar un valor, {:get, sender} para obtener el resultado.
# No se comparten variables globales; todo pasa por mensajes.
# Se lanza 2 procesos (con spawn) que iteran sobre tasks y envían {:add, val, self()} al actor.
# Resultado: Suma duplicada (igual que en Java). El actor es el único que conserva el estado (current_sum).

defmodule SumActor do
  def loop(current_sum) do
    receive do
      {:add, val, sender} ->
        new_sum = current_sum + val
        send sender, {:ok, new_sum}
        loop(new_sum)
      {:get, sender} ->
        send sender, {:result, current_sum}
        loop(current_sum)
    end
  end
end

defmodule Main do
  def run do
    # Iniciar actor con sum=0
    actor_pid = spawn(SumActor, :loop, [0])
    tasks = [5, 2, 7, 3, 10]

    # Crear 2 procesos que envíen mensajes
    for _ <- 1..2 do
      spawn(fn ->
        Enum.each(tasks, fn val ->
          send(actor_pid, {:add, val, self()})
          receive do
            {:ok, _partial} -> :ok
          end
        end)
      end)
    end

    # Esperar un momento
    Process.sleep(1000)

    # Pedir resultado final
    send(actor_pid, {:get, self()})
    receive do
      {:result, final_sum} ->
        IO.puts("Resultado final (Elixir, actores): #{final_sum}")
    end
  end
end

Main.run()
