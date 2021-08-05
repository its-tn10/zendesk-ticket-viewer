from dotenv import load_dotenv

import json, unittest, utils

load_dotenv()

# These unit tests come with the assumption of the tickets being loaded from the original tickets.json file and no changes have been made.

class TestTicketListingResponse(unittest.TestCase):
    def test_endpoint(self):
        '''Test that the endpoint of get_tickets() is successful.'''

        self.assertEqual(utils.make_request('/api/v2/tickets').status_code, 200)

    def test_equal_requests(self):
        '''Test that get_tickets() works in a normal manner from two requests.'''

        firstRequest = utils.get_tickets()
        secondRequest = utils.get_tickets()

        self.assertEqual(firstRequest, secondRequest)

    def test_listings_data(self):
        '''Test that get_tickets() returns the correct and same data from tickets.json.'''

        newRequest = utils.get_tickets()

        oldRequestFile = open('jsons/ticketRequest.json', 'r')
        oldRequest = json.loads(oldRequestFile.read())
        oldRequestFile.close()

        self.assertEqual(newRequest, oldRequest)

class TestIndividualTicketResponse(unittest.TestCase):
    def test_endpoint(self):
        '''Test that the endpoint of get_ticket() is successful.'''

        self.assertEqual(utils.make_request('/api/v2/tickets/2').status_code, 200)

    def test_equal_requests(self):
        '''Test that get_ticket() works in a normal manner from two requests.'''

        firstRequest = utils.get_ticket(2)
        secondRequest = utils.get_ticket(2)

        self.assertEqual(firstRequest, secondRequest)

    def test_ticket_data(self):
        '''Test that get_ticket() returns the correct and same data from ticket ID #2.'''

        newRequest = utils.get_ticket(2)

        oldRequestFile = open('jsons/ticketIndividualRequest.json', 'r')
        oldRequest = json.loads(oldRequestFile.read())
        oldRequestFile.close()

        self.assertEqual(newRequest, oldRequest)

class TestTicketPagingResponse(unittest.TestCase):
    def test_endpoint(self):
        '''Test that the endpoint of get_page() is successful.'''

        self.assertEqual(utils.make_request('/api/v2/tickets').status_code, 200)

    def test_paging_count(self):
        '''Test that get_page() works in dividing the 100 tickets to 4 pages with 25 tickets each.'''
        pageRequest = [utils.get_page(1), utils.get_page(2), utils.get_page(3), utils.get_page(4)]

        self.assertEqual(len(pageRequest[0]), len(pageRequest[1]))
        self.assertEqual(len(pageRequest[1]), len(pageRequest[2]))
        self.assertEqual(len(pageRequest[2]), len(pageRequest[3]))

    def test_equal_requests(self):
        '''Test that get_page() works in a normal manner from two requests.'''

        firstRequest = utils.get_page()
        secondRequest = utils.get_page()

        self.assertEqual(firstRequest, secondRequest)

    def test_paging_data(self):
        '''Test that get_page() returns the correct and same tickets in the first page.'''

        newRequest = utils.get_page()

        oldRequestFile = open('jsons/ticketPageRequest.json', 'r')
        oldRequest = json.loads(oldRequestFile.read())
        oldRequestFile.close()

        self.assertEqual(newRequest, oldRequest)

if __name__ == '__main__':
    unittest.main()
