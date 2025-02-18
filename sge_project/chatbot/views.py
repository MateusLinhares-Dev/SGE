from django.http import JsonResponse
import json
from .execute_code import chabot_specialist_ia
from rest_framework.views import APIView
from products.models import Product

class ChatbotAPIView(APIView):
    queryset = Product.objects.all()

    def post(self, request):
        dados = json.loads(request.body)
        pergunta = dados.get("mensagem", "")
        usuario = dados.get("usuario", "amigo")

        resposta = chabot_specialist_ia(pergunta)

        return JsonResponse({"resposta": f"Olá, {usuario}! {resposta}"})