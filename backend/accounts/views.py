from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(["GET"])
def status(request: Request):
    return Response(data={"status": "Working"})


@api_view(["POST"])
def singup(request: Request):
    pass
