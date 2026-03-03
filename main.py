from fastapi import FastAPI

from api.books import router as books_router


# Crear instancia principal de la aplicación FastAPI.
# 'app' será utilizada por Uvicorn para levantar el servidor.
app = FastAPI(
    title="API Personal Library",
    description="Backend REST with FastAPI for managing books.",
    version="1.0.0"
)

# Endpoint de prueba (ruta raíz).
@app.get("/")
def root():
    """
    Endpoint to confirm that the API is running. It returns a simple JSON message indicating that the library API is functioning correctly.
    """
    return {"mensaje": "API of personal library is running!"}

# Include the books router to handle all book-related endpoints under the /api/libros prefix.
app.include_router(books_router)