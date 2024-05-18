import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the name parameter from the query string
    name = req.params.get('name')

    if not name:
        try:
            # If the name parameter is not found, try getting it from the request body
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # If a name is provided, return a personalized greeting
        return func.HttpResponse(f"Hello, {name}!")
    else:
        # If no name is provided, return a default greeting
        return func.HttpResponse("Hello, World!", status_code=200)
