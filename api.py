from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
from sections import sections  # Import sections from the new file

app = FastAPI()
class Section(BaseModel):
    id: str
    title: str
    content: str
    tags: list[str]

# Basic routes
@app.get("/")
async def root():
  return {"message": "Welcome to FastAPI"}

@app.get("/sections/")
async def get_sections():
    return sections

@app.get("/sections/{section_id}")
async def get_section(section_id: str):
    if section_id in sections:
        return sections[section_id]
    return {"error": "Section not found"}

@app.post("/sections/{section_id}")
async def update_section(section_id: str, section: Section):
    if section_id in sections:
        sections[section_id] = {
            "title": section.title,
            "content": section.content,
            "tags": section.tags
        }
        return {"message": "Section updated successfully"}
    return {"error": "Section not found"}

@app.post("/sections/")
async def add_section(section: Section):
    if section.id in sections:
        return {"error": "Section with this ID already exists"}
    sections[section.id] = {
        "title": section.title,
        "content": section.content,
        "tags": section.tags
    }
    return {"message": "Section added successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)