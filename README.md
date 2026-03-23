# Login Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. You must execute the command: `docker-compose -f dev.docker-compose.yml up --force-recreate` in the terminal
9. Use `python app.py` or `python -m src` to execute the program

NOTE: You have to be standing in the folder containing the: `dev.docker-compose.yml` and you need to install `Docker Desktop` if you are in Windows.

### Pre-Commit for Development

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

I made a python program using tkinter as user interface. Basically I made a login system in which if you don't have an account you can register. It will ask you for a username and password, use mongo db to store the information in a database and werkzeug for password encryption. It is very useful to access a program that is protected by this login, if you have an account you will be able to access the program, otherwise you will not be able to.

## Technologies used

1. Python >= 3.11
2. Tkinter
3. Docker
4. MongoDB

## Libraries used

#### Requirements.txt

```
pymongo==4.10.1
werkzeug==3.1.6
pydantic==2.11.9
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
```

#### Requirements.test.txt

```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt

```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Login-Program`](https://www.diegolibonati.com.ar/#/project/Login-Program)

## Video

https://user-images.githubusercontent.com/99032604/199149396-0e2f1703-c84e-4278-ac90-e806f0aba018.mp4

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `MONGO_HOST`: Specifies the hostname or address where the MongoDB server is located. In this case, `host.docker.internal` allows a Docker container to connect to the host machine.
3. `MONGO_PORT`: Defines the port on which the MongoDB server is listening for connections. The default MongoDB port is `27017`.
4. `MONGO_USER`: Indicates the username for authenticating with the MongoDB database.
5. `MONGO_PASS`: Contains the password associated with the user specified in `MONGO_USER` for authentication.
6. `MONGO_DB_NAME`: Specifies the name of the database to which the application will connect within the MongoDB server.
7. `MONGO_AUTH_SOURCE`: Defines the database where the user credentials will be verified. Typically set to `admin` when the credentials were created in that database.

```
ENVIRONMENT=development

MONGO_HOST=host.docker.internal
MONGO_PORT=27017
MONGO_USER=admin
MONGO_PASS=secret123
MONGO_DB_NAME=login_db
MONGO_AUTH_SOURCE=admin
```

## Known Issues

None at the moment.