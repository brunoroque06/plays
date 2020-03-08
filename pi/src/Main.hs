module Main where

import Pi
import System.Environment
import System.Random

main :: IO ()
main = do
  gen <- newStdGen
  args <- getArgs
  let numPoints = if (length args) == 0 then 1000 else read . head $ args :: Int
  print . calculateRatio . isPointInsideCircle . take numPoints . createPoint $ randoms gen
