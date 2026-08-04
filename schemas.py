from pydantic import BaseModel, field_serializer, field_validator, Field

class schemapersonBeas(BaseModel):
    name:str= Field(..., description="Enter person name ")
    @field_validator("name")
    def name_validat(cls, value):
        if len(value) > 32:
            raise ValueError("name is too larg")
        if not value.isalpha():
            raise ValueError("name is most be alphabetic ch")
        return value
    @field_serializer("name")
    def serializer_name(self, value):
        return value.title()
class schemapersonCreate(schemapersonBeas):
    pass

class schemaperResponse(schemapersonBeas):
    id:int=Field(..., deprecated="this is uniq id")

class schemapersonUpdate(schemapersonBeas):
    pass


