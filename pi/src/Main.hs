module Main where

import Pi
import Points

main :: IO ()
main = do
  putStrLn "Running Monte Carlo's method to estimate π. Number of points:"
  numPoints <- readLn
  putStrLn "Generating coordinates..."
  randomNumbers <- randomList 0 1
  let coordinates = take (numPoints * 2) $ randomNumbers
  putStrLn "Creating Points..."
  let points = createPoints coordinates
  putStrLn "Estimating π..."
  print $ estimatePi points
