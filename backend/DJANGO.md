# Setting Up Django Project

## Step 1: Create a Virtual Environment

Navigate to the backend directory and run the following command:

```bash
python3 -m venv venv
```

## Step 2: Activate Virtual Environment

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

You should see (venv) appear at the beginning of your command prompt, indicating that the virtual environment is active.

## Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

## Step 4: Run the Server

```bash
python manage.py runserver
```

By default, the server will run on <http://127.0.0.1:8000/>.

## Step 5: Deactivate Virtual Environment

```bash
deactivate
```
