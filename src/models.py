from pydantic import BaseModel


class Function_calling_test(BaseModel):
    prompt: str


class Parameter(BaseModel):
    type: str


class Returns(BaseModel):
    type: str


class Function_definition(BaseModel):
    name: str
    description: str
    parameters: dict[str, Parameter]
    returns: Returns
