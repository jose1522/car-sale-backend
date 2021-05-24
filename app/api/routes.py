from fastapi import APIRouter, Depends
from database import validation, models
from core.routerDependencies import oauth2_scheme, user_login
from core.util.authentication import get_current_user
from typing import Optional

apiRouter = APIRouter()


@apiRouter.get('/')
async def index():
    return {"hello" : "world updated 2"}


# @apiRouter.get('/test', dependencies=[Depends(user_login)])
@apiRouter.get('/test')
async def test(user = Depends(user_login)):
    return user


@apiRouter.post('/authenticate')
async def getUser(inputCredentials: validation.AuthParams):
    result = await models.User.authenticate(inputCredentials)
    return result


################################################################
# User-related endpoints
################################################################


@apiRouter.post('/user')
async def newUser(newUser: validation.NewUserParams):
    result = await models.User.createUser(newUser)
    return result


@apiRouter.get('/user', dependencies=[Depends(user_login)])
# @apiRouter.get('/user')
async def getUserData(user = Depends(user_login)):
    return user

@apiRouter.put('/user', dependencies=[Depends(user_login)])
# @apiRouter.put('/user')
async def updateUser(data: validation.UserParams, user = Depends(user_login)):
    result = await models.User.updateUser(user, data)
    return result

@apiRouter.delete('/user', dependencies=[Depends(user_login)])
# @apiRouter.delete('/user')
async def deleteUser(user = Depends(user_login)):
    result = await models.User.deleteUser(user)
    return result


################################################################
# Car-related endpoints
################################################################

@apiRouter.get('/car', dependencies=[Depends(user_login)])
# @apiRouter.get('/car')
async def getUserData(carID: Optional[str] = None):
    if carID == "all" or carID == "" or not carID:
        result = await models.Car.getAll()
    else:
        result = await  models.Car.getById(carID)
    return result

@apiRouter.post('/car', dependencies=[Depends(user_login)])
# @apiRouter.post('/car')
async def newCar(newCar: validation.NewCarParams):
    result = await models.Car.createCar(newCar)
    return result

@apiRouter.put('/car', dependencies=[Depends(user_login)])
# @apiRouter.put('/car')
async def updateCar(data: validation.CarParams):
    result = await models.Car.updateCar(data)
    return result

@apiRouter.delete('/car', dependencies=[Depends(user_login)])
# @apiRouter.delete('/car')
async def deleteCar(data: validation.CarParams):
    result = await models.Car.deleteCar(data)
    return result