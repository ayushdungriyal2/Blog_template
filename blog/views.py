from django.shortcuts import render
from .models import SinlgeBlogInfo, WebsiteInfo, Category
from django.http import HttpResponse

# home


def Home(request):

    WebsiteData = WebsiteInfo.objects.all()
    CategoryData = Category.objects.all()
    SinlgeBlogInfoData = SinlgeBlogInfo.objects.all()
    Context = {"SinlgeBlogInfoData": SinlgeBlogInfoData,"WebsiteData": WebsiteData, "CategoryData": CategoryData}
    return render(request, 'blog/index.html', Context)

def CategoryUrl(request, str):
    WebsiteData = WebsiteInfo.objects.all()
    CategoryData = Category.objects.all()
    SinlgeBlogInfoData = SinlgeBlogInfo.objects.all().filter(Category__Name = str)
    Context = {"SinlgeBlogInfoData": SinlgeBlogInfoData,"WebsiteData": WebsiteData, "CategoryData":CategoryData}    
    return render(request, 'blog/index.html', Context)


def FromString(request, str):

    WebsiteData = WebsiteInfo.objects.all()
    CategoryData = Category.objects.all()
    SinlgeBlogInfoData = SinlgeBlogInfo.objects.all().filter(Slug=str)

    # interlinking 
    
    Id = SinlgeBlogInfo.objects.filter(Slug=str).values_list('id')

    if Id[0][-1] :
        Interlinking_id = 1
        BlogInterlinking = SinlgeBlogInfo.objects.all().filter(id=Interlinking_id)
        Context = {"SinlgeBlogInfoData": SinlgeBlogInfoData, "WebsiteData": WebsiteData,"BlogInterlinking": BlogInterlinking,"CategoryData":CategoryData}
        return render(request, 'blog/single-blog-page-template.html', Context)

    else:
        print(Id[0][-1])
        Interlinking_id = Id[0][0] + 1
        BlogInterlinking = SinlgeBlogInfo.objects.all().filter(id=Interlinking_id)
        Context = {"SinlgeBlogInfoData": SinlgeBlogInfoData, "WebsiteData": WebsiteData,"BlogInterlinking": BlogInterlinking,"CategoryData":CategoryData}
        return render(request, 'blog/single-blog-page-template.html', Context)
