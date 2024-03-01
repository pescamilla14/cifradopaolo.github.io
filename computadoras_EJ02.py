""""
29/02/2024
Alejandro Paolo Escamilla Trujillo
Uso de fastApi para crear una pagina de computadoras
"""


from typing import List
from fastapi import FastAPI, Query, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Tienda de tecnología"
app.version = "0.0.1"

# Se define una lista de diccionarios, cada uno representando una computadora con sus características como ID, RAM, almacenamiento, marca y modelo. 
# Esta lista actúa como una base de datos que nos servida para el ejemplo.

computadoras = [
    {"id": 1, "ram": "16GB", "almacenamiento": "1TB", "marca": "Asus", "modelo": "ROG"},
    {"id": 2, "ram": "8GB", "almacenamiento": "250GB", "marca": "Apple", "modelo": "Pro"},
    {"id": 3, "ram": "16GB", "almacenamiento": "3TB", "marca": "Hp", "modelo": "Minium"},
    {"id": 4, "ram": "8GB", "almacenamiento": "512GB", "marca": "Acer", "modelo": "Predator"},
    {"id": 5, "ram": "16GB", "almacenamiento": "1TB", "marca": "Dell", "modelo": "M7"},
    
]
# Ese define un endpoint / que devuelve un mensaje de bienvenida en formato HTML. 
# Este es un buen ejemplo de cómo personalizar la respuesta para devolver diferentes tipos de contenido, con una respuesta HTMLResponse.

@app.get("/", response_class=HTMLResponse, tags=["home"])
async def message():
    return "<h1>Bienvenido a la Tienda de Tecnología</h1>"

# aqui buscaremos la computadora con su ID asignado dando un caso donde no se encuentre la consola dira "Computadora no encontrada"
# Utiliza una búsqueda lineal en la lista de computadoras para encontrar la correspondiente.

@app.get("/computadoras/{computadora_id}", tags=["computadora"])
def get_computadora(computadora_id: int):
    for computadora in computadoras:
        if computadora["id"] == computadora_id:
            return computadora
    return {"mensaje": "Computadora no encontrada"}

@app.get("/computadoras/buscar", tags=["busqueda"])
def buscar_computadoras(marca: str = Query(None), modelo: str = Query(None)):
    resultados = computadoras  
    
    

    if marca:
        resultados = [comp for comp in resultados if comp['marca'].lower() == marca.lower()]
    if modelo:
        resultados = [comp for comp in resultados if comp['modelo'].lower() == modelo.lower()]

    return resultados if resultados else {"mensaje": "No se encontraron computadoras con esos criterios"}
    
# permite a los usuarios crear una nueva computadora enviando detalles. Esto demuestra cómo recibir y manejar datos

@app.post('/computadoras',tags=['computadoras'])
def create_computadora(id: int = Body(), tittle: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    computadoras.append({
        "id": id,
        "tittle": tittle,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category,
    })
    return computadoras


# definir un endpoint para editar una computadora existente
@app.put("/computadoras/{computadoras_id}" ,tags=["computadoras"])
def edit_editarcompu(id: int = Body(), tittle: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    computadoras.append({


    })