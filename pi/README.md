# Estimation of π Using Monte Carlo Method

Given a square containing a circle, with a radius of half the size of the square's side, the following is true:

$$ \frac{ π . r^2 }{ A_r } = \frac{ P_i }{ P_t } \implies π = \frac{ A_r . P_i }{ r^2 . P_t } $$

where:

- $r$, circle's radius;
- $A_r$, rectangle's area;
- $P_i$, number of points inside the circle;
- $P_t$, total number of points.

The points above mentioned are randomly placed in the square, and therefore the precision of the estimation increases with the number of points.
