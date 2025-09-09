from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models.colleges import CollegeScreen, College, GrantsScreen
from app.data.college_data import colleges_data, grants_list, general_rules

router = APIRouter()

@router.get("/colleges", response_model=CollegeScreen)
async def get_colleges ():
    data = list(colleges_data.values())
    return CollegeScreen(colleges=data, total_colleges=len(data))

@router.get("/colleges/{college_id}", response_model=College)
async def get_college(college_id: str):
    college = colleges_data.get(college_id)
    if not college:
        raise HTTPException(status_code=404, detail="College not found")
    return college

@router.get("/grants", response_model=GrantsScreen)
async def get_grants():
    return GrantsScreen(grants=grants_list, rules=general_rules)