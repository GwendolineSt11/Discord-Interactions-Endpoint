from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from django.http import JsonResponse

def discord_endpoint(request):
    verify_key = VerifyKey(bytes.fromhex('68a897f3fcc0821311abfc807a9dea42b303525d2cfe444d499d39af8d41d36a'))
    signature = request.headers["X-Signature-Ed25519"]
    timestamp = request.headers["X-Signature-Timestamp"]
    body = request.body.decode("utf-8")

    try:
        verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
        return JsonResponse({'type':1})
    except BadSignatureError:
        return JsonResponse({'error': 'Invalid request signature'}, status=405)
