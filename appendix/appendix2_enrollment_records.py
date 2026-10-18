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


# ---------- 2. University Enrollment Records ----------
def merge(a, b):
    out, i, j, c = [], 0, 0, 0
    while i < len(a) and j < len(b):
        c += 1
        if a[i] <= b[j]: out.append(a[i]); i += 1
        else:            out.append(b[j]); j += 1
    out += a[i:] + b[j:]
    return out, c

print("\n=== 2. University Enrollment Records ===")
A = [SEED_DIGIT + ID_SUM * i for i in range(NAME_LENGTH)]
B = [NAME_LENGTH + ARTIST_LENGTH * i for i in range(ARTIST_LENGTH)]
merged, comps = merge(A, B)
print("Department A :", A)
print("Department B :", B)
print("Consolidated :", merged)
print(f"Records before: {len(A)} + {len(B)} = {len(A)+len(B)} | after: {len(merged)}")
print("Comparisons  :", comps)
print("Order correct:", merged == sorted(A + B) and len(merged) == len(A) + len(B))
print("Complexity   -> O(n + m) time, O(n + m) space")
