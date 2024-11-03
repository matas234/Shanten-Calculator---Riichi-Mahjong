import time
from shanten_calculator import calculateShanten

def webToArray(hand_string):
    cur_arr = []
    out_arr = [[0]*9 for _ in range(3)] + [[0]*7]

    suit_to_idx = {'m': 0, 'p': 1, 's': 2, 'z': 3}

    for chr in hand_string:
        if chr in ['s', 'm', 'p', 'z']:
            suit_idx = suit_to_idx[chr]
            for tile_idx in cur_arr:
                out_arr[suit_idx][tile_idx - 1] += 1
            cur_arr = []

        else:
            cur_arr.append(int(chr))

    return out_arr


arrays = []
failed = 0
passed = 0
with open('shanten_tests.txt', 'r') as f:
    for line in f:  
        line = line.strip()
        hand_string, true_shanten = line.split(" ")
        hand_array = webToArray(hand_string)
        arrays.append(hand_array)
        calculated_shanten = calculateShanten(hand_array)

        # print(f"hand: {hand_string}")
        # print(f"true shanten: {true_shanten}")
        # print(f"calculated shanten: {calculated_shanten}")
        # print("")

        if calculated_shanten == int(true_shanten):
            passed += 1
        else:
            failed += 1

    print(f"passed: {passed}")
    print(f"failed: {failed}")