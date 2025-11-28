import time

def main():
    try:
        with open("testi\\testi.txt", "r", encoding="utf-8") as f:
            for rivi in f:
                print("uusi rivi")
                print(rivi.strip())
    except FileNotFoundError:
        print("File not found – check the path.")
    except OSError:
        print("Tarkistatko vielä funktion parametrit.")

    
if __name__ == "__main__":
    main()