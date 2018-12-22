from django.http import JsonResponse


def users(request):
    response = {'code': 1000, 'data': None}
    response['data'] = [
        {
            'name': 'gzy',
            'age': 22
        },
        {
            'name': 'ggg',
            'age': 11
        },
        {
            'name': 'zzz',
            'age': 10
        },
    ]
    return JsonResponse(response)