"""
This file provides a skeleton for receiving messages from
the Bandwidth messaging API via a POST request, and fowarding that message
through some means of communication.

JSON fields for the POST request from the Bandwidth messaging API can be found at
https://dev.bandwidth.com/ap-docs/apiCallbacks/sms.html
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def get_destination_and_message(post_request):
    """
    Takes a POST request and extracts the message and destination from it.
    
    :post_request A Django POST HttpRequest

    :return [:String, :String] The destination and message from the text

    Example for extracting the destination and message from a Bandwidth POST request
    in the format
    "<destination><space><message>" (example: "jmulford@bandwidth.com Hello Jacob"):
        json_request = json.loads(post_request.body)
        source_text = json_request["text"]

        return source_text.split(' ', 1)

    """

    #Your code here
    pass

def send_message(message, destination):
    """
    Sends the message to its destination

    :message The message to be sent
    :destination The destination of the message

    This function can be defined in many ways using many APIs based
    on the requirements of your application.

    Example for sending a text message using the Bandwidth messaging API:
        messaging_api = messaging.Client(USER_ID, API_TOKEN, API_SECRET)
        messaging_api.send_message(
            from_ = BANDWIDTH_NUMBER,
            to = destination,
            text = message
        )
    """

    #Your code here
    pass

@csrf_exempt
def forward_bandwidth_message(request):
    if request.method == "GET":
        return HttpResponse('hello')

    elif request.method == "POST":
        #Get destination and message from the POST request
        [destination, message] = get_destination_and_message(request)
        
        #Send your message via some means of communication
        send_message(message, destination)

        return HttpResponse("success")
