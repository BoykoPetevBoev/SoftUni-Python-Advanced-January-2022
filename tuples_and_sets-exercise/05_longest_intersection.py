lines = int(input())

longest_intersection = []

for _ in range(lines):
        first_data, second_data  = input().split("-")

        first_start, first_end = first_data.split(",")
        first_range = set(range(int(first_start), int(first_end) + 1))

        second_start, second_end = second_data.split(",")
        second_range = set(range(int(second_start), int(second_end) + 1))

        intersection = first_range.intersection(second_range)

        if len(longest_intersection) < len(intersection):
            result = []
            for num in intersection:
                result.append(str(num))
            longest_intersection = result

print(f"Longest intersection is [{', '.join(longest_intersection)}] with length {len(longest_intersection)}")



