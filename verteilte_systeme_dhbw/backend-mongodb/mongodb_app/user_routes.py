from fastapi import APIRouter, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from . import models

from . import crud

router = APIRouter()


@router.post("/connect/", response_description="creates a new user", status_code=status.HTTP_200_OK,
             response_model=models.User)
def create_new_user(request: Request):
    user = crud.create_new_user(request)
    # verify_user = crud.verify_user(request, user.id)
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="User creation failed.")


@router.put("/level/update/", response_description="update user level", status_code=status.HTTP_200_OK,
            response_model=models.Message)
def update_user_level(request: Request, user_id: str, level_adjustment: int):
    # raise http exception, if level_adjustment is not -1 or 1
    if level_adjustment not in (-1, 1):
        raise HTTPException(status_code=403, detail="Only a level adjustment of +/- 1 is allowed.")

    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    user = crud.update_user_level(request, user, level_adjustment)
    if user:
        return models.Message(message="Level successfully updated.")
    else:
        raise HTTPException(status_code=403, detail="User level not in range 1-5.")


@router.get("/level/get/", response_description="get user", status_code=status.HTTP_200_OK,
            response_model=models.User)
def get_user(request: Request, user_id: str):
    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    return user


@router.delete("/delete/", response_description="delete user", status_code=status.HTTP_200_OK,
               response_model=models.Message)
def delete_user(request: Request, user_id: str):
    user = crud.verify_user(request, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"No user with user_id={user_id} found.")

    user = crud.delete_user(request, user)
    if user:
        return models.Message(message=f"User with user_id={user_id} successfully deleted.")
    else:
        raise HTTPException(status_code=400, detail=f"User with user_id={user_id} could not be deleted.")
