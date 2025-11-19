import time

def main():
    print("Ohjelma käynnissä. Paina Ctrl+C lopettaaksesi.")
    try:
        while True:
            # Tee jotain tai odota
            print("Suoritetaan...")
            time.sleep(1)  # Odottaa 1 sekunnin
            pass  # Tyhjä silmukka
    except KeyboardInterrupt:
        print("\nKeskeytetty. Suljetaan ohjelma.")

if __name__ == "__main__":
    main()