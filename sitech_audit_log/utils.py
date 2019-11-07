def get_user_ip(request):
    if request:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
           return x_forwarded_for.split(',')[0]
        else:
            return request.META.get('REMOTE_ADDR')
    return None


def get_user_agent(request):
    if request:
        return request.META['HTTP_USER_AGENT']
    return None
