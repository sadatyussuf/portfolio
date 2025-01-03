from django.shortcuts import render

# Create your views here.


def homepage_view(request):
    return render(request, "pages/landing.html")


# def project_view(request):
#     return render(request, "pages/projects.html")


# def project_detail_view(request, uid):

#     return render(request, "pages/project-blog.html")
