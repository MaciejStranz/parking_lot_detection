# 🚗 Analiza Zajętości Miejsc Parkingowych przy użyciu YOLO i SSD

Projekt ma na celu analizę zajętości miejsc parkingowych na podstawie zdjęć z lotu ptaka, przy użyciu nowoczesnych metod detekcji obiektów – **YOLO** oraz **SSD**. Przetwarzane są obrazy przedstawiające parkingi w różnych warunkach pogodowych oraz pod różnymi kątami, a wynik stanowi wizualizacja zajętości z informacją liczbową.

## 📌 Motywacja

Efektywne zarządzanie parkowaniem wpływa bezpośrednio na:
- płynność ruchu,
- zanieczyszczenie powietrza,
- komfort życia mieszkańców.

Celem projektu jest stworzenie systemu, który automatycznie wykryje i oceni zajętość miejsc parkingowych, a także umożliwi analizę wzorców parkowania.

---

## 🗂️ Dane wejściowe i wyjściowe

**Dane wejściowe:**
- Zdjęcia z drona (różne kąty, różne warunki pogodowe)
- Zbiór danych: **PKLot**

**Dane wyjściowe:**
- Obraz z naniesionymi ramkami zaznaczającymi miejsca parkingowe
- Kolorowe oznaczenia: `zajęte` / `wolne`
- Liczbowy wynik zliczający wolne i zajęte miejsca

---

## 🧾 Zbiór danych: PKLot

Zbiór **PKLot** zawiera:

- 12 416 zdjęć JPEG (1280×720 px)
- 695 335 ręcznie oznaczonych miejsc parkingowych
  - 48,6% zajęte
  - 51,4% wolne
- Dane z dwóch parkingów i trzech różnych kątów
- Oznaczenia pogodowe: `sunny`, `rainy`, `cloudy`
- Podział:
  - 70% trening
  - 20% walidacja
  - 10% test

Przykładowe zdjęcie z datasetu:

![PKLot example](original.jpg)

---

## ⚙️ Użyte metody

### 🧠 You Only Look Once (YOLO)

YOLO to szybka, jednoprzebiegowa sieć do detekcji obiektów. Działa na zasadzie podziału obrazu na siatkę, a każda komórka przewiduje pozycje oraz klasy obiektów.

#### Zalety YOLO:
- ⚡ Bardzo szybkie działanie (real-time)
- 🎯 Wysoka dokładność
- 🔄 Kontekst całego obrazu brany pod uwagę
- 📉 Mniej fałszywych pozytywnych detekcji

#### Proces:
1. Podział obrazu na siatkę
2. Predykcja bounding boxów + klasy
3. Skalowanie ramek
4. Non-Maximum Suppression (NMS)

YOLO świetnie sprawdza się w detekcji miejsc parkingowych na zdjęciach PKLot – radzi sobie z różnymi kątami, rozmiarami oraz złożonym tłem.

---

### 📦 Single Shot MultiBox Detector (SSD)

SSD to także metoda jednoprzebiegowa, bazująca na konwolucyjnych mapach cech i kotwicach (default boxes), z których każda przewiduje obecność obiektu.

#### Architektura:
- Ekstraktor cech (np. VGG16, ResNet)
- Warstwy Multibox (predykcja klasy + offset pozycji)

#### Proces:
1. Ekstrakcja map cech
2. Kotwice (różne rozmiary i proporcje)
3. Predykcja klas i offsetów
4. Non-Maximum Suppression (NMS)

#### Zalety SSD:
- 🔥 Real-time performance
- 🧩 Detekcja obiektów o różnych rozmiarach
- 🛠️ Prosta implementacja

W kontekście projektu SSD skutecznie identyfikuje miejsca parkingowe niezależnie od skali i perspektywy, oferując równowagę między prędkością a precyzją.

---

## 🧪 Podział zbioru

| Zbiór        | Liczba obrazów | Procentowy udział |
|--------------|----------------|--------------------|
| Treningowy   | 6891           | 70%                |
| Walidacyjny  | 2483           | 20%                |
| Testowy      | 1242           | 10%                |

---

## 📊 Wyniki Modelu YOLO

Model **YOLO** osiągnął wysoką dokładność w detekcji miejsc parkingowych, szczególnie w zakresie średnich i dużych obiektów.

### Average Precision (AP):
- **AP (IoU=0.50:0.95)**: `0.833` – solidna ogólna wydajność.
- **AP (IoU=0.50)**: `0.986` – bardzo dokładne wykrywanie przy luźniejszych kryteriach.
- **AP (IoU=0.75)**: `0.979` – model utrzymuje wysoką precyzję przy bardziej rygorystycznych progach.
- **AP (medium)**: `0.832` – dobra wydajność przy średnich obiektach.
- **AP (large)**: `0.857` – dobra skuteczność przy większych obiektach.

### Average Recall (AR):
- **AR (maxDets=1)**: `0.026` – model ma trudności przy pojedynczych obiektach.
- **AR (maxDets=10)**: `0.217` – poprawa przy większej liczbie detekcji.
- **AR (maxDets=100)**: `0.877` – bardzo dobra skuteczność przy pełnej detekcji.
- **AR (medium)**: `0.877`
- **AR (large)**: `0.889`

### Podsumowanie:
Model YOLO pokazuje bardzo wysoką skuteczność przy większej liczbie detekcji oraz wysoką precyzję niezależnie od IoU. Nadaje się do praktycznych zastosowań w systemach monitorowania parkingów.

---

## 📊 Wyniki Modelu SSD

Model **SSD** uzyskał jeszcze wyższe wyniki w wielu metrykach, zwłaszcza przy średnich i dużych obiektach.

### Average Precision (AP):
- **AP (IoU=0.50:0.95)**: `0.904` – bardzo wysoka ogólna skuteczność.
- **AP (IoU=0.50)**: `0.984` – znakomita dokładność.
- **AP (IoU=0.75)**: `0.979` – utrzymuje wysoką precyzję również przy bardziej restrykcyjnych progach.
- **AP (small)**: `0.834` – dobra wydajność przy mniejszych obiektach.
- **AP (medium)**: `0.931`
- **AP (large)**: `0.984`

### Average Recall (AR):
- **AR (maxDets=1)**: `0.028` – ograniczona skuteczność przy pojedynczych detekcjach.
- **AR (maxDets=10)**: `0.231` – nieco lepiej, ale wciąż niższa skuteczność.
- **AR (maxDets=100)**: `0.931` – bardzo wysoka skuteczność przy większej liczbie detekcji.
- **AR (small)**: `0.872`
- **AR (medium)**: `0.957`
- **AR (large)**: `0.992`

### Podsumowanie:
Model SSD wykazuje **wyjątkową dokładność i skuteczność**, szczególnie w wykrywaniu obiektów średnich i dużych. Dzięki wysokim wartościom AP i AR sprawdzi się w systemach rozpoznawania miejsc parkingowych z dużą dokładnością.

---

## 🏁 Wnioski

Oba modele – **YOLO** i **SSD** – osiągają bardzo wysoką skuteczność w detekcji miejsc parkingowych, jednak:
- YOLO lepiej radzi sobie przy różnych wartościach IoU, ale ma nieco niższy AR.
- SSD dominuje w dokładności i skuteczności przy większych obiektach i liczbach detekcji.

Wybór modelu zależy od konkretnego zastosowania: SSD może być preferowany do dokładniejszych aplikacji z pełną detekcją, podczas gdy YOLO sprawdzi się dobrze w szybkich, mniej obciążających systemach.

---

