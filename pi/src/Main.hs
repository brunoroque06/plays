module Main where

import Pi
import Points

main :: IO ()
main = do
  putStrLn "Using Monte Carlo's method to estimate π. Number of points?"
  numPoints <- readLn
  points <- take numPoints <$> randomPoints
  print $ approximatePi points
