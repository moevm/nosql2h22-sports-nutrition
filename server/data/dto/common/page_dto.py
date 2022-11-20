from pydantic import BaseModel, Field


class PageDto(BaseModel):
    page: int = Field(..., description='Page must be a positive value', gt=0)
    size: int = Field(..., description='Size must be a positive value', gt=0)
