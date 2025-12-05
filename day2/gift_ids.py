input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
ranges = [r.strip() for r in input.split(",")]


def validate_gift_id(gift_id: int) -> bool:
    str_id = str(gift_id)
    first_half = str_id[: len(str_id) // 2]
    second_half = str_id[len(str_id) // 2 :]

    # return true if the first half is not in the second half
    return first_half not in second_half


invalid_ids = []
for gift_ids in ranges:
    start = int(gift_ids.split("-")[0])
    end = int(gift_ids.split("-")[1])

    for gift_id in range(start, end + 1):
        if len(str(gift_id)) % 2 != 0:
            # Gift ID is not even length, skip
            continue

        if not validate_gift_id(gift_id):
            # print(f"Invalid gift ID found: {gift_id}")
            invalid_ids.append(gift_id)

print(f"Total invalid gift IDs found: {len(invalid_ids)}")
# print(f"Invalid gift IDs: {invalid_ids}")
print(f"Sum of invalid gift IDs: {sum(invalid_ids)}")
