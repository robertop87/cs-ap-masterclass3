-- Haskell (uso de Control.Concurrent.STM para transacciones).

-- newTVarIO crea un TVar (variable transaccional) para total.
-- Se define worker que recorre tasks y, en cada iteración, hace atomically { readTVar, calcular, writeTVar }.
-- STM se encarga de la consistencia: si varios hilos actualizan el TVar, sus transacciones se serializan automáticamente.
-- Resultado: Suma duplicada de los valores.

import Control.Concurrent
import Control.Concurrent.STM
import Control.Monad (forM_)

main :: IO ()
main = do
  totalTVar <- newTVarIO (0 :: Int)
  let tasks = [5, 2, 7, 3, 10]

  let worker = do
        forM_ tasks $ \val -> do
          threadDelay 50000  -- simulando trabajo
          atomically $ do
            current <- readTVar totalTVar
            let newSum = current + val
            writeTVar totalTVar newSum

  -- Crear 2 hilos
  forkIO worker
  forkIO worker

  -- Esperar un poco para terminar
  threadDelay 1000000  -- 1 segundo

  finalSum <- readTVarIO totalTVar
  putStrLn $ "Resultado final (Haskell STM): " ++ show finalSum
