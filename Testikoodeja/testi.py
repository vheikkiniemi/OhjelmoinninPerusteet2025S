users = ["alice", "bob", "root1", "carl"]

for u in users:
    if u == "root":
        print("Admin löytyi!")
        break
else:
    print("Adminia ei löytynyt.")