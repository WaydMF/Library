from django.shortcuts import redirect


def redirect_library(request):
    return redirect('library_url', permanent=True)
