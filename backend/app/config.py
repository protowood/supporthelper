import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    app_host: str = os.getenv('APP_HOST', '127.0.0.1')
    app_port: int = int(os.getenv('APP_PORT', '8080'))
    log_level: str = os.getenv('LOG_LEVEL', 'info')
    database_url: str = os.getenv('DATABASE_URL', 'postgresql+psycopg://supporthelper:password@localhost:5432/supporthelper')
    db_pool_size: int = int(os.getenv('DB_POOL_SIZE', '5'))
    db_pool_max_overflow: int = int(os.getenv('DB_POOL_MAX_OVERFLOW', '10'))
    default_connector: str = os.getenv('DEFAULT_CONNECTOR', 'mimir_alertmanager')
    cors_origins: list[str] = os.getenv('CORS_ORIGINS', 'http://localhost').split(',')
    mimir_alertmanager_base_url: str = os.getenv('MIMIR_ALERTMANAGER_BASE_URL', 'http://localhost:8081')
    mimir_alertmanager_auth_token: str | None = os.getenv('MIMIR_ALERTMANAGER_AUTH_TOKEN')

settings = Settings()
