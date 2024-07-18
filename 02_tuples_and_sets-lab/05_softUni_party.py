# from collections import deque

guests = int(input())
reservation_codes = set()

for _ in range(guests):
    code = input()
    reservation_codes.add(code)

guest_code = input()

while guest_code != "END":
    if guest_code in reservation_codes:
        reservation_codes.remove(guest_code)
    guest_code = input()

print(len(reservation_codes))

if reservation_codes:
    print("\n".join(sorted(reservation_codes)))