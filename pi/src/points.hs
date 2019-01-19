module Points where

import Control.Arrow (Arrow, (***), arr)
import System.Random (newStdGen, randoms)

type Point a = (a, a)

chunk2 :: [a] -> [(a, a)]
chunk2 [] = []
chunk2 [_] = error "list of uneven length"
chunk2 (x:y:r) = (x, y) : chunk2 r

both :: Arrow arr => arr a b -> arr (a, a) (b, b)
both f = f *** f

unsplit :: Arrow arr => (a -> b -> c) -> arr (a, b) c
unsplit = arr . uncurry

randomFloats :: IO [Float]
randomFloats = randoms <$> newStdGen

randomPoints :: IO [Point Float]
randomPoints = chunk2 <$> randomFloats
