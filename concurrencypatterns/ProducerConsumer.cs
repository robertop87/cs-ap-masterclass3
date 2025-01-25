// BufferBlock y ActionBlock representan el patrón.

using System;
using System.Threading.Tasks.Dataflow;

class ProducerConsumer {
    static void Main() {
        var bufferBlock = new BufferBlock<int>();
        var consumerAction = new ActionBlock<int>(item => {
            Console.WriteLine($"Consumidor recibió: {item}");
        });

        // Enlazar el bloque buffer al action
        bufferBlock.LinkTo(consumerAction, new DataflowLinkOptions { PropagateCompletion = true });

        // Productor
        for(int i=0; i<5; i++){
            bufferBlock.Post(i);
        }
        bufferBlock.Complete();

        consumerAction.Completion.Wait();
        Console.WriteLine("Fin del ejemplo Productor-Consumidor en C#");
    }
}
