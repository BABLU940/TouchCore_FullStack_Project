from django.urls import path
# from .views import upload_video, add_subtitle # get_subtitles,search_subtitles
from .views import TouchCore

urlpatterns = [
    path('p/upload_video',TouchCore.as_view({'get': 'upload_video'})),
    path('p/add_subtitle', TouchCore.as_view({'post':'add_subtitle' })),
    path('p/subtitles/<int:video_id>', TouchCore.as_view({'get':'subtitles'})),
    path('p/search_subtitles/<int:video_id>',TouchCore.as_view({'get':'search_subtitles'})),

]

