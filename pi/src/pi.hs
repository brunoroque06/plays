module Pi where

import System.Random
import Data.List (foldl')

isPointInsideCircle :: [(Double, Double)] -> (Int, Int)
isPointInsideCircle = foldl' pythagoras (0, 0)

pythagoras :: (Int, Int) -> (Double, Double) -> (Int, Int)
pythagoras (ins, total) (x, y) = (ins + if x ** 2 + y ** 2 <= 1 then 1 else 0, total + 1)

calculateRatio :: (Int, Int) -> Double
calculateRatio (ins, total) = (4 * fromIntegral ins / fromIntegral total)

display:: (Int, Int) -> String
display (heads, coins) = "π = " ++ (show $ 4.0 * fromIntegral heads / fromIntegral coins)

createPoint :: [Double] -> [(Double, Double)]
createPoint (a : b : r) = (a, b) : createPoint r
