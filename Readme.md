## Project setup
### 1. Setup virtual environment
(python version == 3.10.8)
```bash
python3 -m venv .venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install relevant packages
```
pip install -r requirements.txt
```

### 3: run project
```
uvicorn main:app --reload 

or

fastapi dev main.py
```

### 4: Swagger ui
```
http://localhost:8000/docs
```