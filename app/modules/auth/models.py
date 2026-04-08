# app/modules/auth/models.py
# Импорты для колонок SQLAlchemy (String=текст, Integer=число, ForeignKey=внешний ключ)
from sqlalchemy import String, Integer, Boolean, ForeignKey
# Импорты для ORM связей (Mapped=типизация, relationship=связь таблиц)
from sqlalchemy.orm import Mapped, mapped_column, relationship
# Base — наша базовая модель из app/core/db.py (наследуем от неё)
from app.core.db import Base

# Таблица sp_users — основные данные пользователя
class User(Base):
    __tablename__ = "sp_users"  # Имя таблицы в PostgreSQL
    
    # id — PRIMARY KEY (автоинкремент 1,2,3...), index для быстрых SELECT
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    # email — уникальный, индексированный, обязательный (VARCHAR 255)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    
    # hashed_password — bcrypt хэш пароля (VARCHAR 1024), обязательный
    hashed_password: Mapped[str] = mapped_column(String(1024), nullable=False)
    
    # is_active — булево, по умолчанию True (активный аккаунт)
    is_active: Mapped[bool] = mapped_column(default=True)
    
    # profile — связь 1:1 с таблицей Profile (один user = один профиль)
    profile: Mapped["Profile"] = relationship(back_populates="user")

# Таблица sp_profiles — дополнительная информация пользователя
class Profile(Base):
    __tablename__ = "sp_profiles"  # Имя таблицы в PostgreSQL
    
    # id — PRIMARY KEY (автоинкремент)
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # user_id — FOREIGN KEY на sp_users.id, CASCADE=удаляем при удалении user
    user_id: Mapped[int] = mapped_column(ForeignKey("sp_users.id", ondelete="CASCADE"))
    
    # firstname — имя пользователя (VARCHAR 50), может быть NULL
    firstname: Mapped[str | None] = mapped_column(String(50))
    
    # country_code — код страны (RU, US, CN), по умолчанию "RU"
    country_code: Mapped[str] = mapped_column(String(2), default="RU")
    
    # user — обратная связь 1:1 с таблицей User
    user: Mapped[User] = relationship(back_populates="profile")