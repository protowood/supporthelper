from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List
from fastapi import APIRouter
from ..connectors.mimir_alertmanager import MimirAlertmanagerConnector

router = APIRouter(prefix='/alerts', tags=['alerts'])

executor = ThreadPoolExecutor(max_workers=8)

@router.get('/fetch')
async def fetch_alerts() -> List[Dict[str, Any]]:
	connector = MimirAlertmanagerConnector()
	return await _run_in_pool(connector.fetch_alerts)

@router.post('/forward')
async def forward_alerts(alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
	connector = MimirAlertmanagerConnector()
	return await _run_in_pool(lambda: connector.send_alerts(alerts))

async def _run_in_pool(func):
	import asyncio
	loop = asyncio.get_running_loop()
	return await loop.run_in_executor(executor, func)
