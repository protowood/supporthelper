from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
	'app_requests_total',
	'Total number of HTTP requests',
	['method', 'path', 'status']
)

REQUEST_LATENCY = Histogram(
	'app_request_latency_seconds',
	'Latency of HTTP requests in seconds',
	['method', 'path']
)
