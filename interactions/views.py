from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from urllib.request import urlopen
from discord_interaction import urls
import json
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def interactions_view(request):
    if request.method == 'POST':
        try:
            raw_body = request.body.decode('utf-8')  # Decode byte string to UTF-8
            logger.info(f"Received raw body: {raw_body}")
            data = json.loads(raw_body)
            logger.info(f"Received data: {data}")
            if data.get('PING') == 1:
                response_payload = {
                    "PONG": 1,
                    "token": data.get("token"),
                }
                return JsonResponse(response_payload)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error(f"Internal Server Error: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    else:
        if request.method == 'GET':
            return HttpResponse("Hello, this is the interaction endpoint! You made it!")
        else:
            logger.warning("Invalid request method received")
            return JsonResponse({'error': 'Invalid request method'}, status=405)

