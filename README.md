# README

## Opis projektu

Jest to biblioteka zawierająca funkcje pomocnicze do różnych zastosowań, takich jak:
- Normalizacja danych,
- Obliczanie silni,
- Obliczanie n-tego wyrazu ciągu Fibonacciego,
- Zliczanie samogłosków i słów w tekście.


## Instalacja

### 1. Klonowanie repozytorium


```bash
git clone https://github.com/twoje_repozytorium.git 
```
### 2. Funkcje biblioteki

1. normalize_data(data)
Funkcja normalize_data normalizuje dane wejściowe (listę liczb) do zakresu [0, 1].

Argumenty:
data (list): Lista liczb, które mają zostać znormalizowane.
Zwracane:
Lista liczb w zakresie [0, 1].
Przykład:
```python
from TestLib.data_utils import normalize_data

data = [10, 20, 30]
normalized_data = normalize_data(data)
print(normalized_data)  # Output: [0.0, 0.5, 1.0]
```
2. factorial(n)
Funkcja factorial oblicza silnię liczby n.

Argumenty:
n (int): Liczba, dla której obliczana jest silnia.
Zwracane:
Liczba całkowita - wynik obliczenia silni.
Przykład:
```python
from TestLib.math_tools import factorial

print(factorial(5))  # Output: 120
```
3. fibonacci(n)
Funkcja fibonacci oblicza n-ty element ciągu Fibonacciego.

Argumenty:
n (int): Numer wyrazu ciągu Fibonacciego.
Zwracane:
Liczba całkowita - n-ty element ciągu Fibonacciego.
Przykład:
```python
from TestLib.math_tools import fibonacci

print(fibonacci(5))  # Output: 3
```
4. count_vowels(text)
Funkcja count_vowels zlicza liczbę samogłoskowych liter w tekście.

Argumenty:
text (str): Tekst, w którym mają zostać policzone samogłoski.
Zwracane:
Liczba całkowita - liczba samogłoskowych liter.
Przykład:
```python
from TestLib.text_processing import count_vowels

print(count_vowels("Hello World"))  # Output: 3
```
5. count_words(text)
Funkcja count_words zlicza liczbę słów w podanym tekście.

Argumenty:
text (str): Tekst, w którym mają zostać policzone słowa.
Zwracane:
Liczba całkowita - liczba słów.
Przykład:
```python
from TestLib.text_processing import count_words

print(count_words("Python is awesome"))  # Output: 3
```

### 6. **`standardize_data(data)`**

Funkcja `standardize_data` standaryzuje dane wejściowe (listę liczb) do postaci, w której mają one średnią 0 i odchylenie standardowe 1.

#### Argumenty:
- `data` (list): Lista liczb, które mają zostać wystandaryzowane.

#### Zwracane:
- Lista liczb po standaryzacji (średnia = 0, odchylenie standardowe = 1).

#### Przykład:

```python
from TestLib.data_utils import standardize_data

data = [10, 20, 30]
standardized_data = standardize_data(data)
print(standardized_data)  # Output: [-1.0, 0.0, 1.0]
