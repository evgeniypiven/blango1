from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def post_table(request):
    return render(
        request, "blog/post-table.html", {"post_list_url": reverse("post-list")}
    )