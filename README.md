## Shanten calculor
This is my implementation of a riichi mahjong shanten calculator in Python. The algorithm employs a recursive depth-first search with memoization on the different suits of the hand to find the optimal "split". Note, the honours are trivial as they can only form pairs and triplets.
Once the "split" has been found, the problem is trivial as there is a "simple" formula for the shanten (see: https://riichi.wiki/Shanten).
The formula doesnt account for pair presence though so there is a +1 when (taatsus + pairs >= 5 - groups) and (no pair).

## Install
Simply copy the shanten_calculator.py. No requirements or dependancies except Python.


## Testing
My algorithm is similar to https://github.com/Kraballa/ShantenCalculator, however I did discover this repository only after having had written mine. I did use their testing file though.
Tenhou also provides a good testing platform: https://tenhou.net/2/?q=11123345678999s1z. If your run test.py you will see that the program calculates shanten correctly for all 34 cases, and it's (probably) correct in general.

## Usage
Shanten_calculator.py contains the calculateShanten functions. The input is the hand represented as a 2d list of each suit, each index in the subarrays being the number of tiles of that number.
Currently the file performs caching, which is signifantly faster if you're doing a lot of shanten calculations. However, the speed is roughly the same for a single call.
