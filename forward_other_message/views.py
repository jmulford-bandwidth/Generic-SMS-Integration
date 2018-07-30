"""
This file provides a skeleton for receiving messages from
some source of communication via a POST request, and forwarding
that message via the Bandwidth messaging API.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bandwidth import messaging

import os

USER_ID = os.environ['USER_ID']
API_TOKEN = os.environ['API_TOKEN']
API_SECRET = os.environ['API_SECRET']


def get_destination_and_message(post_request):
    """
    Takes a POST request and extracts the message and destination from it.

    :post_request A Django POST HttpRequest

    :return [:String, :String] The destination and message from the POST request

    Example for extracting the destination and message from a Bandwidth POST request
    in the format
    <destination><space><message> (example: "+12345 Hello world"):
        json_request = json.loads(post_request.body)
        source_text = json_request["text"]

        return source_text.split(' ', 1)
    """

    #Your code here
    pass

def get_source_number():
    """
    Returns the Bandwidth number used to send the SMS

    :return :String Bandwidth number
    """
    pass

@csrf_exempt
def forward_other_message(request):
    if request.method == "GET":
        return HttpResponse('hello')

    elif request.method == "POST":
        #Get destination and message from the POST request
        [destination, message] = get_destination_and_message(request)

        #Set up messaging client
        messaging_client = messaging.Client(USER_ID, API_TOKEN, API_SECRET)
        source_number = get_source_number()

        #Send message
        messaging_client.send_message(
            from_ = source_number,
            to = destination,
            text = message
        )

        return HttpResponse("success")
