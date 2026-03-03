from fastapi import FastAPI

from api.books import router as books_router


# Crear instancia principal de la aplicación FastAPI.
# 'app' será utilizada por Uvicorn para levantar el servidor.
app = FastAPI(
    title="API Biblioteca Personal",
    description="Backend REST con FastAPI para gestionar libros.",
    version="1.0.0"
)

# Endpoint de prueba (ruta raíz).
@app.get("/")
def root():
    """
    Endpoint básico que confirma que la API está funcionando.
    """
    return {"mensaje": "API Biblioteca funcionando correctamente"}

# Include the books router to handle all book-related endpoints under the /api/libros prefix.
app.include_router(books_router)