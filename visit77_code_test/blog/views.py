from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import BlogPostSerializer

# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# class UploadImagesView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
            
#             channel_layer = get_channel_layer()
#             async_to_sync(channel_layer.group_send)(
#                 "uploads",
#                 {
#                     "type": "upload_notification",
#                     "content": {"message": "New images uploaded!"}
#                 }
#             )
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    # return HttpResponse('<h1><b> Visit 77 Coding test for Backend Development..  😉</b></h1>')
    return render(request, 'blog/index.html')