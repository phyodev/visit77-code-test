import os, django
import json
import base64
import uuid
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.db import database_sync_to_async

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visit77_code_test.settings')
django.setup()

from .models import BlogPost

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.connect()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'mesage': 'You are now connected'
        }))

class UploadConsumer(AsyncWebsocketConsumer):

    async def receive(self, text_data):
        data = json.loads(text_data)

        images = data.get('images', [])
        if len(images) == 2:
            image_objects = []
            for image in images:
                format, imgstr = image.split(';base64,') 
                ext = format.split('/')[-1] 
                img_data = ContentFile(base64.b64decode(imgstr), name=f"{uuid.uuid4()}.{ext}")
                image_objects.append(img_data)

            if data.get('post_id'):
                blog_post = await self.update_data(data['post_id'], image_objects)
                await self.send(text_data=json.dumps({
                    'message': 'Images updated successfully!',
                    'post_id': blog_post.id
                }))
            else:
                blog_post = await self.save_data(image_objects)
                await self.send(text_data=json.dumps({
                    'message': 'Images uploaded successfully!',
                    'post_id': blog_post.id
                }))
        else:
            await self.send(text_data=json.dumps({
                'error': 'Please upload exactly two images.'
            }))
    
    async def save_data(self, images):
        blog_post = await database_sync_to_async(BlogPost.objects.create)(image1=images[0], image2=images[1])
        return blog_post
    
    async def update_data(self, post_id, images):
        # Retrieve the BlogPost object and update it
        blog_post = await database_sync_to_async(BlogPost.objects.get)(id=post_id)
        if len(images) == 1:  # Only update one image
            blog_post.image1 = images[0]
        elif len(images) == 2:  # Update both images
            blog_post.image1 = images[0]
            blog_post.image2 = images[1]

        await database_sync_to_async(blog_post.save)()  # Save the updated BlogPost
        return blog_post