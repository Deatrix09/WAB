from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware


GOOGLE_CLIENT_ID = "532769069906-93fk839glfu2nmlgfej5cttuumgqb3mf.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"



app = FastAPI()
app.add_middleware(SessionMiddleware,secret_key="123456789yxcvbnm")





config_data = {
    'GOOGLE_CLIENT_ID' : GOOGLE_CLIENT_ID,
    'GOOGLE_CLIENT_SECRET' : GOOGLE_CLIENT_SECRET
}

starlette_cnfg = Config(environ=config_data)
outh = OAuth(starlette_cnfg)

outh.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        'scope': 'openid email profile'
    }
)

@app.get("/")
async def home():
    return HTMLResponse(
        '''

            <body>
                <a href="/login"> Login </a>
            </body>

        '''
        )


@app.get("/login")
async def login(
    request: Request
):
    return await outh.google.authorize_redirect(request,"http://localhost:8000/token")


@app.get("/token")
async def token(request : Request):
    state = request.query_params.get("state")
    access_token  = await outh.google.authorize_access_token(request)
    return  access_token['id_token']