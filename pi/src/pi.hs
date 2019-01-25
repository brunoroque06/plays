module Pi where

import Points

estimatePi :: [Point] -> Double
estimatePi points = 4 * pointsIn' / totalPoints'
  where pointsIn' = fromIntegral(sum (numberOfPointsIn points))
        totalPoints' = fromIntegral(length points) 

numberOfPointsIn :: [Point] -> [Int]
numberOfPointsIn points = map isPointInsideCircle points

isPointInsideCircle :: Point -> Int
isPointInsideCircle (x, y) = mapBool pythagoras'
  where pythagoras' = sqrt(x ** 2 + y ** 2) <= 1

mapBool :: Bool -> Int
mapBool bool | bool == False = 0
             | otherwise = 1
