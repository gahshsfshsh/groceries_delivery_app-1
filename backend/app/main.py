from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Groceries Delivery App API",
    description="Backend для мобильного приложения доставки продуктов",
    version="0.1.0"
)

# CORS для поддержки мобильного Flutter frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для мобильного клиента оставить*, для продакшена — ограничить
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/status")
def status():
    """Проверка работоспособности backend"""
    return {"status": "ok", "message": "Backend FastAPI работает"}

# TODO: подключить маршруты категорий, товаров, заказов, аутентификации
