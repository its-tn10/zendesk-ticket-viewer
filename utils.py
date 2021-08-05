from errors import APIError

import base64, os, requests

def make_request(endpoint):
    auth_str = base64.b64encode((os.environ.get('ZENDESK_EMAIL') + '/token:' + os.environ.get('ZENDESK_TOKEN')).encode()).decode()
    response = requests.get(os.environ.get('ZENDESK_DOMAIN') + endpoint, headers={'Authorization': 'Basic ' + auth_str})
    if response.status_code >= 400:
        raise APIError()
    return response

def get_tickets():
    return make_request('/api/v2/tickets').json()['tickets']

def get_ticket(ticket_id):
    return make_request('/api/v2/tickets/' + str(ticket_id)).json()['ticket']

def get_page(page = 1):
    tickets = get_tickets()
    pages = (len(tickets) // 25) + 1

    if 1 <= page <= pages:
        lowerBound = (page - 1) * 25
        higherBound = lowerBound + 25
        
        return tickets[lowerBound:higherBound]

    raise ValueError()