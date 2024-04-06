from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from . import models

from . import crud

router = APIRouter()


@router.get("/connect/", response_description="creates a new user", status_code=status.HTTP_200_OK,
            response_model=models.User)
def create_new_user(request: Request):
    user = crud.create_new_user(request)
    # verify_user = crud.verify_user(request, user.id)
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="User creation failed.")


