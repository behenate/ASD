"""
W ramach obchodów międzynarodowego święta cyklistów organizatorzy przewidzieli górską
wycieczkę rowerową. Będzie się ona odbywać po bardzo wąskiej ścieżce, na której rowery mogą
jechać tylko jeden za drugim. W ramach zapewnienia bezpieczeństwa każdy rowerzysta będzie
miał numer identyfikacyjny oraz małe urządzenie, przez które będzie mógł przekazać
identyfikator rowerzysty przed nim (lub -1 jeśli nie widzi przed sobą nikogo). Należy napisać
funkcję, która na wejściu otrzymuje informacje wysłane przez rowerzystów i oblicza rozmiar
najmniejszej grupy (organizatorzy obawiają się, że na małe grupy mogłyby napadać dzikie
zwierzęta). Dane są następujące struktury danych:
struct Cyclist {
int id, n id; // identyfikator rowerzysty oraz tego, którego widzi
};
Funkcja powinna mieć prototyp int smallestGroup( Cyclist cyclist[], int n ), gdzie
cyclist to tablica n rowerzystów. Funkcja powinna być możliwie jak najszybsza. Można założyć,
że identyfikatory rowerzystów to liczby z zakresu 0 do 108
(osiem cyfr napisanych w dwóch
rzędach na koszulce rowerzysty) i że pamięć nie jest ograniczona. Rowerzystów jest jednak dużo
mniej niż identyfikatorów (nie bez powodu boją się dzikich zwierząt). Należy zaimplementować
wszystkie potrzebne struktury danych.

"""
test = [0 for _ in range(10**8)]
""" ¯\_(ツ)_/¯ """
