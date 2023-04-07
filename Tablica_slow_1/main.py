import os

# Funkcja zwracająca ścieżkę do pliku w zależności od wybranego poziomu trudności
def get_file_path(level):
    if level == 'latwy':
        return 'easy_PL.txt'
    elif level == 'sredni':
        return 'medium_PL.txt'
    elif level == 'trudny':
        return 'hard_PL.txt'
    else:
        return None

# Funkcja zwracająca listę słów z pliku tekstowego + polskie znaki
def get_words_from_file(file_path):
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
        return words

# Pytanie użytkownika o poziom trudności i pobranie ścieżki do pliku
level = input("Wybierz poziom trudności (latwy/sredni/trudny): ")
file_path = get_file_path(level)

# Pobranie listy słów z pliku tekstowego
words = get_words_from_file(file_path)

# Wyświetlenie listy słów
if words:
    print(" ".join(words))
else:
    print("Nie można otworzyć pliku o podanej ścieżce.")