import os
import hashlib

print("🚀 PyDupeFinder Start Aagudhu...")

folder = "/storage/emulated/0/DupeTest"
os.makedirs(folder, exist_ok=True)

data = "Elango Project Mass!" * 10000
with open(f"{folder}/file1.txt", "w") as f: f.write(data)
with open(f"{folder}/file2.txt", "w") as f: f.write(data)
print("✅ Test files ready: file1.txt, file2.txt")

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

print("\n🔍 Scanning for duplicates...")
hashes = {}
for file in os.listdir(folder):
    path = os.path.join(folder, file)
    h = get_hash(path)
    if h in hashes:
        hashes[h].append(path)
    else:
        hashes[h] = [path]

found = False
total_waste = 0
for paths in hashes.values():
    if len(paths) > 1:
        found = True
        size = os.path.getsize(paths[0])
        waste = size * (len(paths) - 1)
        total_waste += waste
        print(f"\n⚠️ Found {len(paths)} copies:")
        for p in paths: print(f" - {p}")
        print(f"💾 Wasted Space: {waste/1024:.2f} KB")

if not found:
    print("🎉 No duplicates found!")

print(f"\n💾 Total Wasted: {total_waste/1024/1024:.2f} MB")