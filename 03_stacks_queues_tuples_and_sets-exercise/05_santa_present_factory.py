def present_crafting(materials, magic_values):
    presents = {}
    while materials and magic_values:
        m = materials.pop()
        for i, magic in enumerate(magic_values):
            if magic * m in [150, 250, 300, 500]:
                if magic * m == 150:
                    if "doll" in presents:
                        presents["doll"] += 1
                    else:
                        presents["doll"] = 1
                elif magic * m == 250:
                    if "train" in presents:
                        presents["train"] += 1
                    else:
                        presents["train"] = 1
                elif magic * m == 300:
                    if "teddy bear" in presents:
                        presents["teddy bear"] += 1
                    else:
                        presents["teddy bear"] = 1
                elif magic * m == 500:
                    if "bicycle" in presents:
                        presents["bicycle"] += 1
                    else:
                        presents["bicycle"] = 1
                magic_values.pop(i)
                break
            elif magic + m < 0:
                materials.append(magic + m)
                magic_values.pop(i)
                break
            elif m + magic > 0:
                materials[-1] = m + magic
                magic_values.pop(i)
                break
    if "doll" in presents and "train" in presents or "teddy bear" in presents and "bicycle" in presents:
        return "The presents are crafted! Merry Christmas!", materials, magic_values, presents
    else:
        return "No presents this Christmas!", materials, magic_values, presents


materials = list(map(int, input().split()))
magic_values = list(map(int, input().split()))
result, materials, magic_values, presents = present_crafting(materials, magic_values)
print(result)
if materials:
    print("Materials left:", ', '.join(map(str, materials)))
if magic_values:
    print("Magic left:", ', '.join(map(str, magic_values)))
if presents:
    items = list(presents.items())
    items.sort()
    for item, amount in items:
        print("{}: {}".format(item, amount))