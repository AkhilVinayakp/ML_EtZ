import os, requests


def login(request):
    # fn will sent request to corresponding route as part auth service
    # deployed to login the user.
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)

    basicAuth = (auth.username, auth.password)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login", auth=basicAuth
    )
    # !TODO : AUTH_SVC_ADDRESS should be set in the environment.

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)