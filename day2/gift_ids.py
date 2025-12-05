from icecream import ic

input = "5959566378-5959623425,946263-1041590,7777713106-7777870316,35289387-35394603,400-605,9398763-9592164,74280544-74442206,85684682-85865536,90493-179243,202820-342465,872920-935940,76905692-76973065,822774704-822842541,642605-677786,3759067960-3759239836,1284-3164,755464-833196,52-128,3-14,30481-55388,844722790-844967944,83826709-83860070,9595933151-9595993435,4216-9667,529939-579900,1077949-1151438,394508-486310,794-1154,10159-17642,5471119-5683923,16-36,17797-29079,187-382"
ranges = [r.strip() for r in input.split(",")]

ic.disable()


def validate_gift_id(gift_id: int) -> bool:
    str_id = str(gift_id)
    first_half = str_id[: len(str_id) // 2]
    second_half = str_id[len(str_id) // 2 :]
    return first_half not in second_half


invalid_ids = []
for gift_ids in ranges:
    start = int(gift_ids.split("-")[0])
    end = int(gift_ids.split("-")[1])
    for gift_id in range(start, end + 1):
        ic(gift_id)
        ic(len(str(gift_id)))

        if len(str(gift_id)) % 2 != 0:
            ic("Gift ID length is not even:", gift_id)
            continue

        if not validate_gift_id(gift_id):
            # print(f"Invalid gift ID found: {gift_id}")
            invalid_ids.append(gift_id)

print(f"Total invalid gift IDs found: {len(invalid_ids)}")
# print(f"Invalid gift IDs: {invalid_ids}")
print(f"Sum of invalid gift IDs: {sum(invalid_ids)}")
