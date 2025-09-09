from fastapi import APIRouter, Query
from fastapi import HTTPException
from typing import List, Optional, Dict
from app.models.home import HomeScreen
from app.data.university_info import university_info
from app.data.president_message import president_message
from app.data.university_info_en import university_info_en
from app.data.president_message_en import president_message_en

router = APIRouter(prefix="/home", tags=["Home"])

@router.get("/home", response_model=HomeScreen)
async def get_home(
    username: Optional[str] = Query(None, description="Username for greeting"),
    lang: str = Query("arabic", description="Language: arabic or english")
):
    
    if lang == "english":
        uni_data = university_info_en
        pres_msg = president_message_en
        welcome_msg = f"Welcome {username} to Banha National University 🎓" if username else None
        
    elif lang == "arabic":
        uni_data = university_info
        pres_msg = president_message
        welcome_msg = f"مرحبًا يا {username} في جامعة بنها الأهلية 🎓" if username else None

    else:
        raise HTTPException(
        status_code=400,
        detail="Invalid language. Supported values are 'arabic' and 'english'."
    )
    

    
    result = HomeScreen(
        welcome=welcome_msg,
        university=uni_data,
        president_message=pres_msg
    )

    return result
