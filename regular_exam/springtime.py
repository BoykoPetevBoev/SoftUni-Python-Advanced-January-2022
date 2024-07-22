
def start_spring(**kwargs):

    spring_collection = {}
    result = ''

    for key in kwargs:
        object_type = kwargs[key]

        if object_type in spring_collection:
            spring_collection[object_type].append(key)
        else:
            spring_collection[object_type] = [key]

    spring_collection = sorted(spring_collection.items())
    spring_collection = sorted(spring_collection, key=lambda item: len(item[1]), reverse=True)
    spring_collection = dict(spring_collection)

    for key in spring_collection:
        spring_collection[key].sort()
        separator = '\n-'
        result += f"{key}:{separator}"
        result += separator.join(spring_collection[key])
        result += "\n"

    return result

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower"}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird"}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
