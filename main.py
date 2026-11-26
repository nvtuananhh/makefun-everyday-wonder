import os

# The umbrella: a stranger tilts their umbrella over you at the bus
# stop, and for one block the rain behaves like a polite guest.
# The surprise is the last clause - the rain having manners -
# a fresh angle on a small kindness, grounded in one block.
ENTRY = "A stranger's umbrella tilted over my shoulder at the bus stop, and for one block the rain had manners."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
