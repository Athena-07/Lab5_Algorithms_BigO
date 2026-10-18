# ---------- Student-Specific Inputs ----------
LAST_NAME       = "Zozobrado"
STUDENT_ID      = "TUPM-26-1872"
FAVORITE_ARTIST = "Taylor Swift"

SEED_DIGIT    = int(STUDENT_ID[-1])
ID_SUM        = sum(int(c) for c in STUDENT_ID if c.isdigit())
NAME_LENGTH   = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST.replace(" ", ""))
ARTIST_SUM    = sum(ord(c) - 64 for c in FAVORITE_ARTIST.upper() if c.isalpha())

print("=== Student-Specific Inputs ===")
for k in ("SEED_DIGIT", "ID_SUM", "NAME_LENGTH", "ARTIST_LENGTH", "ARTIST_SUM"):
    print(f"{k:14}= {globals()[k]}")


# ---------- 1. Emergency Dispatch Record Search ----------
def linear_search(a, t):
    c = 0
    for i, x in enumerate(a):
        c += 1
        if x == t:
            return i, c
    return -1, c

def rotated_binary_search(a, t):
    lo, hi, c = 0, len(a) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        c += 1
        if a[mid] == t:
            return mid, c
        c += 1
        if a[lo] <= a[mid]:                      # left half sorted
            if a[lo] <= t < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:                                    # right half sorted
            if a[mid] < t <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1, c

print("\n=== 1. Emergency Dispatch Record Search ===")
N = ARTIST_LENGTH + NAME_LENGTH
original = [1000 + ID_SUM + NAME_LENGTH * i for i in range(N)]
rotated  = original[SEED_DIGIT:] + original[:SEED_DIGIT]
target   = original[(ID_SUM + ARTIST_SUM) % N]
print("Original :", original)
print("Rotated  :", rotated)
print("Target   :", target)
pos, c_bin = rotated_binary_search(rotated, target)
_,   c_lin = linear_search(rotated, target)
print("Position :", pos if pos >= 0 else "Not found")
print(f"Comparisons -> Rotated Binary: {c_bin}, Linear: {c_lin}")
print("Complexity  -> Binary: O(log n) time, O(1) space | Linear: O(n) time, O(1) space")
