from fastapi import FastAPI

import api.crud as crud

description = """
โปรเจคง่อย ๆ

ทำสอบไม่ทัน เลยกลับมาทำต่อที่บ้าน

แง ๆ ๆ
"""

app = FastAPI(
    title="aom.elet",
    description=description,
    version="0.0.2",
)


@app.get("/search")
async def search(name: str):
    return crud.search(name)


@app.get("/findall")
def findall():
    return crud.readall()


@app.get("/create")
async def create(name: str, category: str):
    return crud.create(name, category)


@app.get("/update")
async def update(id: str, name: str):
    return crud.update(id, name)


@app.get("/delete")
async def delete(id: str):
    return crud.delete(id)
