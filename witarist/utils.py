
def get_log_string(request):
    method = request.method
    path = request.get_full_path()
    return '-->' + ' ' + method + ' ' + path