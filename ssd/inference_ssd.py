import torch
import torchvision.transforms as transforms
from PIL import Image, ImageDraw
from torchvision.models.detection import ssd300_vgg16

# Ścieżki do modelu i przykładowego obrazu
model_path = "full_model_epoch_75.pth"
#image_path = "data\\test\\images\\2013-01-17_13_45_10.jpg"  # Zamień na ścieżkę do swojego obrazu
#image_path = "data\\test\\images\\2012-09-11_15_27_08.jpg"
image_path ="proba3.jpg"

# Wczytanie modelu na CPU
model = ssd300_vgg16(pretrained=False)
num_classes = 2  # Zmodyfikowane na 2 klasy
model.head.classification_head.num_classes = num_classes

# Wczytanie wag modelu
try:
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    print("Model załadowany poprawnie.")
except Exception as e:
    print(f"Błąd podczas ładowania modelu: {e}")
    exit(1)

model.eval()

# Definicja transformacji obrazu
transform = transforms.Compose([
    transforms.ToTensor()
])

# Funkcja do wykonywania inferencji
def run_inference(image_path, model, transform):
    try:
        # Wczytanie i przetworzenie obrazu
        image = Image.open(image_path).convert("RGB")
        image_tensor = transform(image).unsqueeze(0)  # Dodanie wymiaru batch
        
        # Przesłanie obrazu do modelu
        with torch.no_grad():
            outputs = model(image_tensor)
        
        return outputs, image
    except FileNotFoundError:
        print(f"Plik {image_path} nie został znaleziony.")
        exit(1)
    except Exception as e:
        print(f"Błąd podczas inferencji: {e}")
        exit(1)

# Funkcja do wyświetlania wyników
def display_results(outputs, image):
    draw = ImageDraw.Draw(image)
    for i in range(len(outputs[0]['boxes'])):
        box = outputs[0]['boxes'][i].tolist()
        label = outputs[0]['labels'][i].item()
        score = outputs[0]['scores'][i].item()
        
        if score > 0.01:  # Próg pewności
            if label == 1:
                draw.rectangle(box, outline="green", width=2)
                label_text = "free"
                draw.text((box[0], box[1]), f"{label_text}", fill="green")
            elif label == 2: 
                draw.rectangle(box, outline="red", width=2)
                label_text = "taken"
                draw.text((box[0], box[1]), f"{label_text}", fill="red")
            print(f"Class: {label}, {label_text}")
    
    image.show()

# Wykonanie inferencji
outputs, image = run_inference(image_path, model, transform)

# Wyświetlenie wyników
display_results(outputs, image)
