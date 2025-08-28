from abc import ABC, abstractmethod
from typing import Any, Dict, List

class Connector(ABC):
	@abstractmethod
	def fetch_alerts(self) -> List[Dict[str, Any]]:
		raise NotImplementedError

	@abstractmethod
	def send_alerts(self, alerts: List[Dict[str, Any]]) -> Dict[str, Any]:
		raise NotImplementedError
