# Image Captioning App

This repository contains the **Image Captioning App**, a web application that generates captions for uploaded images using a machine learning model. Built with **Django**, the app integrates a pre-trained model for generating accurate and descriptive captions.

---

## Features
- **Image Upload**: Users can upload images for automatic caption generation.
- **AI-Powered Captions**: Uses a machine learning model to create detailed and context-aware captions.
- **User-Friendly Interface**: Simple and intuitive design for seamless interaction.
- **Data Persistence**: Stores uploaded images and generated captions for future reference.

---

## Project Structure
- **`caption_generator/`**: Core module handling caption generation using the ML model.
- **`image_captioning_app/`**: Main Django app managing views, templates, and the backend logic.
- **`ml_model/`**: Contains the pre-trained model and related utilities for generating captions.
- **`staticfiles/`**: Frontend assets including CSS, JavaScript, and images.
- **`uploads/`**: Directory for storing user-uploaded images.
- **`.gitattributes`**: File attribute management for the repository.
- **`.gitignore`**: Specifies files and directories excluded from version control.
- **`db.sqlite3`**: SQLite database file storing image and caption data.
- **`manage.py`**: Django's management script for running and managing the application.
- **`requirements.txt`**: List of Python dependencies required for the project.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/N2B6/Image_captioning.git
cd image_captioning_app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## How It Works
1. Users upload an image via the app's interface.
2. The image is processed by a pre-trained **machine learning model** located in the `ml_model/` directory.
3. A caption is generated and displayed to the user.
4. Uploaded images and captions are saved in the SQLite database for future reference.

---

## Technologies Used
- **Django**: Web framework for the backend.
- **Python**: Core programming language.
- **Machine Learning**: Pre-trained image captioning model.
- **SQLite**: Lightweight database for storing images and captions.
- **Frontend**: HTML, CSS, and JavaScript for the user interface.

---

## Python Libraries
- **TensorFlow/Keras**: For loading and running the pre-trained model.
- **Pandas**: Data handling and preprocessing.
- **Matplotlib/Seaborn**: Visualizing results (optional).
- **Django**: Backend framework.

---

## Future Enhancements
- **User Authentication**: Allow users to manage their uploaded images and captions.
- **Multiple Language Support**: Generate captions in different languages.
- **Cloud Deployment**: Deploy the app on platforms like AWS, Azure, or Heroku.
- **Improved Model**: Integrate a more advanced model for even better caption accuracy.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributors
- **Nipun Bakshi** – *Developer*
