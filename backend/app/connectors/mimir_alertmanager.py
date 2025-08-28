from typing import Any, Dict, List, Optional
import requests
from .base import Connector
from ..config import settings

class MimirAlertmanagerConnector(Connector):
	def __init__(self, base_url: Optional[str] = None, auth_token: Optional[str] = None) -> None:
		self.base_url = base_url or settings.mimir_alertmanager_base_url
		self.auth_token = auth_token or settings.mimir_alertmanager_auth_token

	def _headers(self) -> Dict[str, str]:
		headers = {'Content-Type': 'application/json'}
		if self.auth_token:
			headers['Authorization'] = f'Bearer {self.auth_token}'
		return headers

	def fetch_alerts(self) -> List[Dict[str, Any]]:
		url = f'{self.base_url}/api/v2/alerts'
		response = requests.get(url, headers=self._headers(), timeout=10)
		response.raise_for_status()
		return response.json()

	def send_alerts(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
		url = f'{self.base_url}/api/v2/alerts'
		response = requests.post(url, json=alerts, headers=self._headers(), timeout=10)
		response.raise_for_status()
		return {'status': 'ok', 'code': response.status_code}
