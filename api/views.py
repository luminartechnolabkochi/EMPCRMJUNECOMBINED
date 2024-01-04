from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response



class EmployeeListCreateView(APIView):

    def get(self,request,*args, **kwargs):
        return Response(data={"message":"listing employees"})
    
    def post(self,request,*args, **kwargs):

        return Response(data={"message":"creating employee"})
    
    
