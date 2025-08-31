from .response_engine import EnhancedResponseEngine

response_engine = EnhancedResponseEngine()

@csrf_exempt
@require_http_methods(["POST"])
def process_text(request):
    try:
        data = json.loads(request.body)
        user_input = data.get('text', '')
        
        # Generate enhanced response
        response = response_engine.generate_response(user_input)
        
        return JsonResponse({
            'status': 'success',
            'response': response
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)