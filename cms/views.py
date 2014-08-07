from django.shortcuts import render_to_response
from django.template import RequestContext
from cms.models import get_banner_images, get_faqs
from cms.models import HomepageInfo
from about.models import get_videos, get_homepage_videos


def index(request):
    images = get_banner_images()
    info = HomepageInfo.objects.get(pk=1)
    videos = get_homepage_videos()
    return render_to_response(
            'cms/index.html',
            {
                'request': request,
                'banner_images': images,
                'info': info,
                'videos': videos,
            },
            RequestContext(request)
        )

def faq(request):
    questions = get_faqs()
    info = HomepageInfo.objects.get(pk=1)
    return render_to_response(
            'cms/faq.html',
            {
                'request': request,
                'questions': questions,
                'info': info,
            },
            RequestContext(request)
        )

