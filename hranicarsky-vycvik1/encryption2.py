# Funkce pro dešifrování textu
# offset se určuje v tomto případě automaticky na základě velikosti písmena
# modulo je operace, která vrací zbytek po dělení dvou čísel, např. 5 % 2 = 1
def decipher(text):
    # Vytváříme prázdný řetězec pro uchování výsledku
    result = ""
    # Iterujeme přes každý znak v daném textu
    for char in text:
        # Pokud je znak číslo
        if char.isdigit():
            # Převedeme znak na číslo, přičteme 5, vezmeme zbytek po dělení 10 (modulo 10)
            # a převedeme zpět na string
            # Takto získáme číslo o 5 vyšší v modulu 10
            result += str((int(char) + 5) % 10)
        # Pokud je znak písmeno
        elif char.isalpha():
            # Nastavíme offset na základě toho, zda je písmeno velké nebo malé
            # ASCII hodnota 'A' je 65 a 'a' je 97
            offset = 65 if char.isupper() else 97
            # Provedeme Caesarovu šifru s posunem 13 na znaku
            # Vezmeme ASCII hodnotu znaku, odečteme offset, přičteme 13, vezmeme modulo 26 a přičteme offset zpět
            result += chr((ord(char) - offset + 13) % 26 + offset)
        # Pokud není znak ani číslo ani písmeno, přidáme ho do výsledku beze změny
        else:
            result += char
    return result

# Kód se vykoná pouze pokud je tento skript spuštěn jako hlavní soubor
if __name__ == "__main__":
    # Definujeme zašifrovaný text
    encoded_text = "XlorePubq{0123456789}"
    # Voláme funkci decipher s zašifrovaným textem a ukládáme výsledek do proměnné decoded_text
    decoded_text = decipher(encoded_text)
    # Vypíšeme dešifrovaný text
    print(f"Výsledek dešifrování: {decoded_text}")