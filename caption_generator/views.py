import os
from django.conf import settings
from django.shortcuts import render
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from PIL import Image
import numpy as np
import pickle
import gdown

from .forms import ImageUploadForm
from .models import UploadedImage

# Define paths for model and tokenizer
model_path = os.path.join(settings.BASE_DIR, 'ml_model/final_model/image_captioning_model_final.keras')
tokenizer_path = os.path.join(settings.BASE_DIR, 'ml_model/final_model/tokenizerfinal.pkl')

# Google Drive file ID for the model
model_file_id = '1CLBi4iAgwewUOWsjqOivANzdGE2yjD01'  # Google Drive file ID for model

# Function to download model from Google Drive if it doesn't exist
def download_from_google_drive(file_id, output_path):
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False)

# Check if the model file exists, otherwise download it
if not os.path.exists(model_path):
    download_from_google_drive(model_file_id, model_path)

model = load_model(model_path)
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

max_length = 82

def extract_features(img_path):
    model_resnet = ResNet50(weights='imagenet')
    model = tf.keras.Model(inputs=model_resnet.input, outputs=model_resnet.layers[-2].output)

    img = Image.open(img_path).resize((224, 224))
    img = np.array(img)
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    features = model.predict(img)
    return features

def generate_caption(model, tokenizer, photo, max_length):
    in_text = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length, padding='post')
        yhat = model.predict([photo, sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = word_for_id(yhat, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'endseq':
            break
    
    # Remove startseq and endseq from the generated caption
    caption = in_text.replace('startseq', '').replace('endseq', '').strip()
    
    return caption

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

from django.http import JsonResponse
from django.shortcuts import render
from .forms import ImageUploadForm
import os
from django.conf import settings

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            img_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.image.name)
            photo = extract_features(img_path)
            caption = generate_caption(model, tokenizer, photo, max_length)
            uploaded_image.caption = caption
            uploaded_image.save()
            return JsonResponse({'caption': caption})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})
