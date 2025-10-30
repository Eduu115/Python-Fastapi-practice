from pydantic import BaseModel

class Ingrediente(BaseModel):

    nombre: str
    calorias: int|None = None # opcional
    carbohidratos: float|None = None # opcional
    proteinas: float|None = None # opcional
    grasas: float|None = None # opcional
    fibra:float|None = None # opcional

class IngredienteParaPlato(BaseModel):
    id:int
    cant:int
    ud:str

class Plato(BaseModel):
    nombre:str
    tipo:str
    ingredientes:list[IngredienteParaPlato]

