from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
	pass

class Alert(Base):
	__tablename__ = 'alerts'
	id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
	fingerprint: Mapped[str] = mapped_column(String(128), unique=True, index=True)
	status: Mapped[str] = mapped_column(String(32))
