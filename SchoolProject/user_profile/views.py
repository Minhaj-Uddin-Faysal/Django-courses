from django.shortcuts import render

# Create your views here.
def profile(request):
    user = request.user
    if profile.objects.filter(user=user).exists():
        profile = profile.objects.get(user=user)
    return render(request, 'profile.html', {'profile': profile})
