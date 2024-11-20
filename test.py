import time
from shanten_calculator import calculateShanten

def webToArray(hand_string):
    cur_arr = []
    out_arr = [0]*34

    suit_to_idx = {'m': 0, 'p': 1, 's': 2, 'z': 3}

    for chr in hand_string:
        if chr in ['s', 'm', 'p', 'z']:
            suit_idx = suit_to_idx[chr]
            for tile_idx in cur_arr:
                out_arr[suit_idx * 9 + tile_idx - 1] += 1

            cur_arr = []

        else:
            cur_arr.append(int(chr))

    return out_arr



failed = 0
passed = 0
with open('shanten_tests.txt', 'r') as f:
    start = time.perf_counter()

    f.seek(0)
    for i in range(10000):
        for line in f:
            line = line.strip()
            hand_string, true_shanten = line.split(" ")
            hand_array = webToArray(hand_string)
            calculated_shanten = calculateShanten(hand_array)

            if calculated_shanten == int(true_shanten):
                passed += 1
            else:
                failed += 1

        f.seek(0)


        end = time.perf_counter()

    print(f"Time: {(end - start) * 1_000:.3f}ms, Average: {(end - start) * 1_000_000 / (passed + failed):.3f}ms per hand")
    print(f"passed: {passed}")
    print(f"failed: {failed}")
