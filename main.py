# 6 backgrounds
# 5 bodies
# 7 eyes
# 5 mouths
# 4 ornaments

# background-->layer-1
# body-->layer-2
# eyes-->layer-3
# mouth-->layer-4
# ornaments-->layer-5
# ------------------------CODE------------------------
from generator import maker

possible_combos = []

for ba in range(1, 7):
    for bo in range(1, 6):
        for ey in range(1, 4):
            for mo in range(1, 5):
                for orn in range(1, 5):
                    possible_combos.append([ba, bo, ey, mo, orn])

count = 1

for combo in possible_combos:
    ba_index = combo[0]
    bo_index = combo[1]
    ey_index = combo[2]
    mo_index = combo[3]
    orn_index = combo[4]
    maker(ba_index, bo_index, ey_index, mo_index, orn_index, count)

    print(f"progress= {count}/1800 ({count/1800 * 100}%)")
    count += 1
