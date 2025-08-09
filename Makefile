install:
	pip install -U pip && pip install -r api/requirements.txt
	cd web && pnpm install

dev-api:
	uvicorn api.main:app --reload --port 8000

dev-web:
	cd web && pnpm dev --port 3000

analyze:
	python api/scripts/analyze.py --video examples/sample.mp4 --out examples/sample.timeline.json
