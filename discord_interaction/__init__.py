from sanic import Sanic
def create_app_instance():
    app = Sanic(name="discord_interaction")
    return app