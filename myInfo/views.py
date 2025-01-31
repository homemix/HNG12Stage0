from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .serializers import InfoSerializer

class GetInfoView(APIView):
    def get(self, request):
        data = {
            "email": "kenmutati@gmail.com",
            "current_datetime": datetime.now(),
            "github_url": "https://github.com/homemix"
        }
        serializer = InfoSerializer(data)
        return Response(serializer.data)