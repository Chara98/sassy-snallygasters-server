"""main server file"""

import fastapi

from .routes import authentication, leaderboard, multiplayer

app = fastapi.FastAPI()

app.include_router(authentication.route)
app.include_router(leaderboard.route)
app.include_router(multiplayer.route)

