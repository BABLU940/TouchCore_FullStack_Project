from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video, Subtitle
from .serializers import SubtitleSerializer
# import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView

class TouchCore(viewsets.ViewSet):


    # @api_view(['POST'])
    def upload_video(self,request):
        video_file = request.FILES.get('video')
        if video_file:

            video = Video.objects.create(file=video_file)
            return JsonResponse({'message': 'Video uploaded successfully.', 'video_id': video.id})
        return JsonResponse({'error': 'No video file was received.'}, status=400)

    @api_view(['POST'])
    def add_subtitle(request):
        video_id = request.data.get('video_id')
        timestamp = request.data.get('timestamp')
        text = request.data.get('text')

        if video_id and timestamp and text:
            try:
                video = Video.objects.get(id=video_id)
                subtitle = Subtitle.objects.create(video=video, timestamp=timestamp, text=text)
                return JsonResponse({'message': 'Subtitle added successfully.', 'subtitle_id': subtitle.id})
            except Video.DoesNotExist:
                return JsonResponse({'error': 'Video not found.'}, status=404)
        return JsonResponse({'error': 'Invalid data provided.'}, status=400)

    @api_view(['GET'])
    def subtitles(request, video_id):
        try:
            video = Video.objects.get(id=video_id)
            subtitles = Subtitle.objects.filter(video=video)
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found.'}, status=404)

    @api_view(['GET'])
    def search_subtitles(request, video_id):
        try:
            video = Video.objects.get(id=video_id)
            search_text = request.query_params.get('q', '').strip()
            if search_text:
                subtitles = Subtitle.objects.filter(video=video, text__icontains=search_text)
            else:
                subtitles = Subtitle.objects.filter(video=video)
            serializer = SubtitleSerializer(subtitles, many=True)
            return Response(serializer.data)
        except Video.DoesNotExist:
            return JsonResponse({'error': 'Video not found.'}, status=404)
