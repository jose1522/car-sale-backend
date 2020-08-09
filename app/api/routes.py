from fastapi import APIRouter, Depends
from database import validation, models
from core.routerDependencies import oauth2_scheme, user_login
from core.util.authentication import get_current_user

apiRouter = APIRouter()

@apiRouter.get('/')
async def index():
    return {"hello" : "world"}


@apiRouter.post('/user')
async def newUser(newUser: validation.NewUserParams):
    result = await models.User.createUser(newUser)
    return result


@apiRouter.put('/user', dependencies=[Depends(user_login)])
async def updateUser(data: validation.UserParams, user = Depends(user_login)):
    result = await models.User.updateUser(user, data)
    return result

@apiRouter.delete('/user', dependencies=[Depends(user_login)])
async def updateUser(user = Depends(user_login)):
    result = await models.User.deleteUser(user)
    return result


@apiRouter.get('/user', dependencies=[Depends(user_login)])
async def getUser(user = Depends(user_login)):
    return user

@apiRouter.get('/authenticate')
async def getUser(inputCredentials: validation.AuthParams):
    result = await models.User.authenticate(inputCredentials)
    return result

@apiRouter.get('/test', dependencies=[Depends(user_login)])
async def test(user = Depends(user_login)):
    return user