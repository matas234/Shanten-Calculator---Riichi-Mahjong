## Shanten calculor
This is my implementation of a riichi mahjong shanten calculator in Python. The algorithm employs a recursive depth-first search on the different suits of the hand to find the optimal "split". Note, the honours are trivial as they can only form pairs and triplets.
Once the "split" has been found, the problem is trivial as there is a "simple" formula for the shanten (see: https://riichi.wiki/Shanten).
The formula doesnt account for pair presence though so there is a +1 when (taatsus + pairs >= 5 - groups) and (no pair).

## Install
Simply copy the shanten_calculator.py. No requirements or dependancies except Python.


## Testing
My algorithm is similar to github.com/Kraballa/ShantenCalculator, however I did discover this repository only after having had written mine. I did use their testing file though.
Tenhou also provides a good testing platform: https://tenhou.net/2/?q=11123345678999s1z.

## Improvements
Caching could be used to greatly improve the overall speed if the function is to be called a lot. However, the overhead is not worth it if only called a few times.
