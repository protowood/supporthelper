from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import alerts
from .metrics import REQUEST_COUNT, REQUEST_LATENCY
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
import time

app = FastAPI(title='SupportHelper Backend')

app.add_middleware(
	CORSMiddleware,
	allow_origins=settings.cors_origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*'],
)

@app.middleware('http')
async def metrics_middleware(request: Request, call_next):
	start = time.perf_counter()
	response = await call_next(request)
	elapsed = time.perf_counter() - start
	path = request.url.path
	method = request.method
	REQUEST_LATENCY.labels(method=method, path=path).observe(elapsed)
	REQUEST_COUNT.labels(method=method, path=path, status=str(response.status_code)).inc()
	return response

@app.get('/metrics')
async def metrics():
	return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get('/health')
async def health():
	return {'status': 'ok'}

app.include_router(alerts.router)

if __name__ == '__main__':
	import uvicorn
	uvicorn.run('app.main:app', host=settings.app_host, port=settings.app_port, reload=True)
