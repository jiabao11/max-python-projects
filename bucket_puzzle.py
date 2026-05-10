print("=" * 45)
print("   Jack's Bucket Puzzle!")
print("=" * 45)
print()
print("Goal: Get exactly 1 liter using")
print("      a 7-liter and a 9-liter bucket.")
print()
print("The 3 rules:")
print("  Rule 1: If 7-bucket is empty  → fill it")
print("  Rule 2: Pour 7-bucket into 9-bucket")
print("  Rule 3: If 9-bucket is full   → empty it")
print()
print("-" * 45)

def solve(bucket7, bucket9, step=1):
    print(f"Step {step:2d}:  7-liter = {bucket7}L   |   9-liter = {bucket9}L")

    # Base case: found 1 liter!
    if bucket7 == 1:
        print()
        print("*** Hooray! We got exactly 1 liter! ***")
        return

    # Rule 1: 7-bucket is empty → fill from tap
    if bucket7 == 0:
        print("         (Rule 1: fill the 7-liter bucket)")
        solve(7, bucket9, step + 1)

    # Rule 3: 9-bucket is full → empty it
    elif bucket9 == 9:
        print("         (Rule 3: empty the 9-liter bucket)")
        solve(bucket7, 0, step + 1)

    # Rule 2: pour from 7-bucket into 9-bucket
    else:
        pour = min(bucket7, 9 - bucket9)
        print(f"         (Rule 2: pour {pour}L into the 9-liter bucket)")
        solve(bucket7 - pour, bucket9 + pour, step + 1)

# Start with both buckets empty
solve(0, 0)

print()
input("Press Enter to quit...")
