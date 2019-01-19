module Pi where

import Control.Arrow ((<<<))
import Data.List (genericLength)
import Points

isInUnitCircle :: (Floating a, Ord a) => Point a -> Bool
isInUnitCircle (x, y) = x' + y' < 0.25
  where x' = (x - 0.5) ** 2
        y' = (y - 0.5) ** 2

lengthRatio :: (Fractional c) => [b] -> [b] -> c
lengthRatio = curry (unsplit (/) <<< both genericLength)

approximatePi :: [Point Float] -> Float
approximatePi points = circleRatio * 4.0
  where circlePoints = filter isInUnitCircle points
        circleRatio = circlePoints `lengthRatio` points
