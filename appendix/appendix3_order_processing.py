import random, time

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


# ---------- 3. E-Commerce Order Processing ----------
def bubble(a):
    a, cmp_, mov = a[:], 0, 0
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            cmp_ += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]; mov += 2
    return a, cmp_, mov

def selection(a):
    a, cmp_, mov = a[:], 0, 0
    for i in range(len(a) - 1):
        m = i
        for j in range(i + 1, len(a)):
            cmp_ += 1
            if a[j] < a[m]: m = j
        if m != i:
            a[i], a[m] = a[m], a[i]; mov += 2
    return a, cmp_, mov

def insertion(a):
    a, cmp_, mov = a[:], 0, 0
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0:
            cmp_ += 1
            if a[j] > key: a[j + 1] = a[j]; mov += 1; j -= 1
            else: break
        a[j + 1] = key; mov += 1
    return a, cmp_, mov

print("\n=== 3. E-Commerce Order Processing ===")
N = ARTIST_LENGTH + NAME_LENGTH
orders_sorted = list(range(1001, 1001 + N))
orders_random = orders_sorted[:]
random.Random(ID_SUM + ARTIST_SUM).shuffle(orders_random)
conditions = {"Sorted": orders_sorted,
              "Reverse": orders_sorted[::-1],
              "Random": orders_random}
for name, data in conditions.items():
    print(f"{name:8}: {data}")

print(f"\n{'Condition':9}{'Algorithm':11}{'Comps':>7}{'Moves':>7}{'Time(ms)':>10}  Correct")
for cname, data in conditions.items():
    for aname, fn in (("Bubble", bubble), ("Selection", selection), ("Insertion", insertion)):
        t0 = time.perf_counter()
        res, c, m = fn(data)
        ms = (time.perf_counter() - t0) * 1000
        print(f"{cname:9}{aname:11}{c:>7}{m:>7}{ms:>10.4f}  {res == sorted(data)}")

print("\nBig O: Bubble/Selection/Insertion -> O(n^2) worst & average;")
print("Best case: Bubble (no early exit here) O(n^2), Selection O(n^2), Insertion O(n) on sorted input.")
print("Space: O(1) auxiliary for all three.")
