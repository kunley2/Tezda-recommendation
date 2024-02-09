from src import create_app
#for fast api
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn
import os


api = FastAPI()
flask_app = create_app()

api_route = '/api/v1'

@api.post(f'{api_route}/recommend')
async def company(user_id:str):
    
    return {'result':"result"}

api.mount('/',WSGIMiddleware(flask_app))

if __name__ == '__main__':
    uvicorn.run(api,host='0.0.0.0',port=os.getenv("PORT"))