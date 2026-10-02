from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(_request):
    """Liveness probe: 200 with a tiny JSON body."""
    return Response({"status": "ok"})
