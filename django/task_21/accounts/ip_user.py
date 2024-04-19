from requests import get

# https://www.ipify.org/ ipify API получение ip пользователя
def get_user_ip(request):
    ip = get('https://api.ipify.org').text
    ip_address = '{}'.format(ip)
    return ip_address