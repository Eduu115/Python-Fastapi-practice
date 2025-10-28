from fastapi import FastAPI

# Objeto app de tipo FastApi
app = FastAPI(
    title="FoodAPI",
    version="0.0.2"
)

# Configuracion del api restful

# Endpoint GET /
@app.get("/")
def read_root():
    return {"Hello": "Edu"}

# Endpoint GET /ingredientes
@app.get("/ingredientes")
def read_ingredientes():
    return {"Objeto": "Ingredientes"}

