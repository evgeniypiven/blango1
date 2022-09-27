from django.shortcuts import render

# Create your views here.
def post_table(request):
    return render(request, "blog/post-table.html")