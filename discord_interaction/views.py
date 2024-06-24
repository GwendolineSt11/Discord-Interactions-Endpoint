from venv import logger
from django.http import JsonResponse, HttpResponse
import json

def interactions_view(request):
    if request.method == 'POST':
        try:
            raw_body = request.body.decode('utf-8')  # Decode byte string to UTF-8
            logger.info(f"Received raw body: {raw_body}")
            data = json.loads(raw_body)
            logger.info(f"Received data: {data}")
            data = json.loads(request.body)
            if data.get('type') == 1:
                response_payload = {
                    "type": 1,
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
    return HttpResponse("Interactions endpoint works!")
