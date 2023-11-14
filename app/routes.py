from app.controller import router
BASE_ROUTE = ""



def register_routes(app, root=""):
    app.include_router(router, 
                       prefix=f"{root}",
                       )
    