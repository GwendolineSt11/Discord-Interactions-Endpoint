from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from urllib.request import urlopen
from discord_interaction import urls
import discord_interactions
import json
import logging
import encodings

logger = logging.getLogger(__name__)

@csrf_exempt
def interactions_view(request):
    if request.method == 'POST':
        try:
            raw_body = request.body
            logger.info(f"Received raw body: {raw_body}")
            data = json.loads(raw_body)
            logger.info(f"Received data: {data}")
            received_token = data.get("token")
            logger.info(f"Received token: {received_token}")
            public_key = '68a897f3fcc0821311abfc807a9dea42b303525d2cfe444d499d39af8d41d36a'
            signature = request.headers.get('X-Signature-Ed25519')
            timestamp = request.headers.get('X-Signature-Timestamp')

            discord_interactions.verify_key(raw_body, signature, timestamp, public_key)

            if data['type'] == discord_interactions.InteractionType.PING:
                return JsonResponse({'type': discord_interactions.InteractionResponseType.PONG})
            if data.get('type') == 1:
                response_data = {
                    "type": 1,
                    "token": data.get("token"),
                }
                return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON request'}, status=400)
        except Exception as e:
            logger.error(f"Internal Server Error: {e}")
            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    else:
        if request.method == 'GET':
            return HttpResponse("Hello, this is the interaction endpoint! You made it!")
        if request.method == 'OPTIONS':
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
        else:
            logger.warning("Invalid request method received")
            return JsonResponse({'error': 'Invalid request method'}, status=405)

