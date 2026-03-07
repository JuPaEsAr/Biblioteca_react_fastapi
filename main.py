from fastapi import FastAPI

from api.books import router as books_router

from fastapi.middleware.cors import CORSMiddleware


# Create the FastAPI application instance.
# 'app' This will be the main entry point for the API.
app = FastAPI(
    title="API Personal Library",
    description="Backend REST with FastAPI for managing books.",
    version="1.0.0"
)

origins = [
    "http://localhost:4200",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Endpoint to confirm that the API is running. 
# It returns a simple JSON message indicating that the library API is functioning correctly.
@app.get("/")
def root():
    """
    Endpoint to confirm that the API is running. It returns a simple JSON message indicating that the library API is functioning correctly.
    """
    return {"mensaje": "API of personal library is running!"}

# Include the books router to handle all book-related endpoints under the /api/libros prefix.
app.include_router(books_router)