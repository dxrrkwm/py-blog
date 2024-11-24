from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from blog.models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 5
    queryset = (Post.objects.select_related("owner")
                .order_by("-created_time"))
    model = Post


class PostDetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentaries__user"))
    model = Post


def comment(request: HttpRequest,  pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentary = request.POST.get("commentary")
        if commentary:
            post.commentaries.create(user=request.user, content=commentary)
    return render(request, "blog/post_detail.html", {"object": post})
