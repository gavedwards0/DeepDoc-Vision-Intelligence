from pydantic import BaseModel, Field
from typing import List, Optional

class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float

class MapElement(BaseModel):
    """Schema for historical map features."""
    name: str = Field(description="The name or label of the landmark/feature.")
    type: str = Field(description="The type of feature (e.g., 'building', 'road', 'boundary').")
    coordinates: Optional[List[float]] = Field(description="Approximate lat/long or local coordinates.")
    bbox: BoundingBox

class DocumentData(BaseModel):
    """General schema for technical document extraction."""
    title: str
    author: Optional[str]
    sections: List[str]
    entities: List[str]
