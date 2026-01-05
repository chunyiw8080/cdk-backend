import azure.functions as func
from app.main import app  # 你的 FastAPI app

# 把 FastAPI 挂载到 Azure Functions
asgi_app = func.AsgiMiddleware(app)

@func.function_name(name="http")
@func.route(
    route="{*path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
)
def main(req: func.HttpRequest, context: func.Context):
    return asgi_app.handle(req, context)
