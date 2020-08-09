from fastapi import Header, HTTPException, Depends
from .settings import Settings
from core.util.authentication import get_current_user, oauth2_scheme


async def get_token_header(x_token: str = Header(...)):
    localSettings = Settings()
    if x_token != localSettings.apiToken:
        raise HTTPException(status_code=400, detail='X-Token header invalid')


async def user_login(token: str = Depends(oauth2_scheme)):
    data = await get_current_user(token)
    return data
