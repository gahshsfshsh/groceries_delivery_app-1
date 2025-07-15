from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
      title="Groceries Delivery API",
      description="Backend для мобильного приложения доставки продуктов.",
      version="1.0.0"
)

# CORS настройки (доступ Flutter frontend)
app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"], # TODO: по production ограничить
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"]
)

# --- Заглушки роутов (реализация позже) ---
@app.get("/")
def root():
      return {"msg": "Groceries Delivery API: FastAPI + PostgreSQL"}

# TODO: подключить routers: categories, products, orders, auth
# from .api import categories, products, orders, auth
# app.include_router(categories.router, prefix="/categories", tags=["Категории"])
# app.include_router(products.router, prefix="/products", tags=["Товары"])
# app.include_router(orders.router, prefix="/orders", tags=["Заказы"])
# app.include_router(auth.router, prefix="/auth", tags=["Авторизация"])

# Стартовая точка для локального запуска
if __name__ == "__main__":
      uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
  
