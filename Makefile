

install:
	cd backend && pip install -r requirements.txt
	cd ../frontend && npm install

start:
	cd backend && uvicorn main:app --reload
	cd ../frontend && npm run dev

dev:
	cd frontend && npm run dev