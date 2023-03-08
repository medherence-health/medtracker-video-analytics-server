# MedTracker Video Analytics Server 🚀

### **Introduction: Structuring of API**

- `api_template:` Contains all the API related Code Base.

  - `manage.py:` Only entry point for API. Contains no logic.
  - `.env:` Most important file for your api and contains global configs. Acoid using application/variable level configs here.
  - `application:` It contains all your api related codes and test modules. I prefer keeping application folder at global.
  - `logs`: Logs is self-explanatory. FYI it will not contain any configuration information, just raw logs. Feel free to move according to your comfort but not inside the application folder.
  - `models:` As a part of Machine-Learning/ Deep-Learning app you might need to add model files here or if you have huge files on cloud add symlinks if possibles.
  - `resources:` To store any documentation, application related csv/txt/img files etc.
  - `settings:` Logger/DataBase/Model global settings files in yaml/json format.

- `application:`
  - `main:` priority folder of all your application related code.
    - `🏗 infrastructure:` Data Base and ML/DL models related backbone code
    - `📮 routers:` API routers and they strictly do not contain any business logic
    - `📡 services:` All processing and business logic for routers here at service layer
    - `⚒ utility:`
      - `config_loader` Load all application related config files from settings directory
      - `logger` Logging module for application
      - `manager` A manager utility for Data Related Task which can be common for different services
    - `🐍 config.py:` Main config of application, inherits all details from .env file
  - `test:` Write test cases for your application here.
  - `initializer.py:` Preload/Initialisation of Models and Module common across application. Preloading model improves inferencing.

### Running Locally ? 📍

    ```bash
        pip install -r requirements.txt

        python scripts/download_models.sh

        uvicorn manage:app --host 0.0.0.0 --port 8000

    ```
    OR
    ```bash
        bash scripts/run.sh
    ```

    Import the API collection into insomnia, and Test it 🚀

### Docker Support 🐳

    ```bash
        docker build -t fastapi-image  .
        docker run -d --name fastapi-container -p 8000:8000 fastapi-image
    ```

### Download Image Models

    ```bash
        bash scripts/download_models.sh
    ```

### Results

    ``json
    {
    "message": "video analysed",
    "result": {
    "kissing": 13.440890341065824,
    "fighting": 68.25806427001953,
    "laughing": 18.226162994280457,
    "clapping": 0.05865482428635005,
    "calling": 0.02985033688958083,
    "running": 0.0009125430551648606,
    "dancing": 0.0010029199358996266,
    "cycling": 0.00963106327582444,
    "hugging": 0.00026188072297372855,
    "drinking": 0.00023221400624606758,
    "using-laptop": 0.07236006786115468
    }
    }
    ```

**Notes:** If results include drinking or eating, then the person in the video is probably taking a drug.

**WARNING:** The model is crappy and not accurate
