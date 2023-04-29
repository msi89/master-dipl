# Face Sickness Detection


## Start with docker

Requirements: 
- Docker
- Docker-compose

Start 

```bash
docker-compose up
```

visit: http://localhost:8000



## Start python virtual environment and nodejs
Python >= 3.9
Nodejs: >= 16.0

```bash
git clone https://github.com/msi89/master-dipl.git facesickness
```


Start backend

```bash
cd facesickness 
python3 -m virtualenv venv && source virtualenv/bin/activate
```

```bash
cd backend 
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0
```

Start frontend

```bash
cd frontend
npm install
echo "VITE_APP_API_URL=http://localhost:8000" > .env
npm run  dev
```

visite: http://localhost:3000