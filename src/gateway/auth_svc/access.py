import os, requests

def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing crednetials", 400)
    
    basicAuth = (auth.username, auth.password)
    
    response = requests.post(
        f"http://{os.environ['AUTH_SVC_ADDRESS']}/login",
        auth=basicAuth
    )
    
    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)