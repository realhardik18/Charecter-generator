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

possible_combos = []

for ba in range(1, 7):
    for bo in range(1, 6):
        for ey in range(1, 4):
            for mo in range(1, 5):
                for orn in range(1, 6):
                    possible_combos.append([ba, bo, ey, mo, orn])
print(possible_combos)
print(f"total combos are: {len(possible_combos)}")
