module Points where

import System.Random (getStdGen, randomRs)

randomList :: Double -> Double -> IO [Double]
randomList min max = getStdGen >>= return . randomRs (min, max)

type Point = (Double, Double)

createPoints :: [Double] -> [Point]
createPoints [] = []
createPoints coords = (coords !! 0, coords !! 1) : createPoints (drop 2 coords)
