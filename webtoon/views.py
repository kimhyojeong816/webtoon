from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .naver_webtoon import *
from .daum_webtoon import *
from django.views.generic import ListView,DetailView
from .models import comment
from django.utils import timezone




# Create your views here.
def naver_webtoon_crw(request):
    naver_webtoon()
    return HttpResponse("네이버 웹툰 크롤링 완료")

def daum_webtoon_crw(request):
    daum_webtoon()
    return HttpResponse("다음 웹툰 크롤링 완료")

class WebtoonList(ListView):
    model = WebToon
    paginate_by=30
    # context_object_name = 'webtoon_list'

    def get_queryset(self):
        query=self.request.GET.get('q')
        if query:
            return WebToon.objects.filter(webtoon_name__contains=query)
        else:
            return WebToon.objects.filter(site_name='네이버')


class DaumWebtoonList(ListView):
    model = WebToon
    paginate_by = 30
    # context_object_name = 'webtoon_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return WebToon.objects.filter(webtoon_name=query)

        else:
                return WebToon.objects.filter(site_name='다음')

class DaumWebtoonList(ListView):
    model = WebToon
    paginate_by=30

    def get_queryset(self):
        return WebToon.object.filter(site_name='다음')

class webtoonDetailView(DetailView):
    model=WebToon

    def get_object(self, queryset=None):
        webtoon_id = self.kwargs["pk"]
        webtoon=WebToon.objects.get(pk=webtoon_id)
        webtoon.webtoon_views += 1
        webtoon.save()

        comment_list=comment.objects.filter(webtoon_id=webtoon_id)
        object={
            "webtoon":webtoon,
            "comment":comment_list
        }
        return object

def addcomment(request,pk):
    comment_object=comment()
    comment_object.webtoon_id=pk
    comment_object.comment_text=request.POST["comment_text"]
    comment_object.create_date_time=timezone.now()
    comment_object.save()

    return HttpResponseRedirect("/detail/"+pk)