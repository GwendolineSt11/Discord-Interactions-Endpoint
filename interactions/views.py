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
def interaction_endpoint(request):
    if request.method == 'POST':
        try:
            raw_body = request.body.decode('utf-8')  # Decode byte string to UTF-8
            logger.info(f"Received raw body: {raw_body}")
            data = json.loads(raw_body)
            logger.info(f"Received data: {data}")
            data = json.loads(request.body)
            if data.get('type') == 1:
                logger.info("Received Discord PING")
                return JsonResponse({"type": 1})

            response_data = {
                "type": 4,
                "data": {
                    "content": "Pong!"
                }
            }
            return JsonResponse(response_data)
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

