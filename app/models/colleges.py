from pydantic import BaseModel
from typing import List

class Grant(BaseModel):
    title: str
    details: str

class College(BaseModel):
    name: str
    programs: List[str]
    tuition_fee: int

class CollegeScreen(BaseModel):
    colleges: List[College]
    total_colleges: int
    
class GrantsScreen(BaseModel):
    grants: List[Grant]
    rules: List[str]