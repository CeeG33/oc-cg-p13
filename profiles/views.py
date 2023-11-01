from django.shortcuts import render, get_object_or_404, get_list_or_404
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Render a list of user profiles.

    This view retrieves a list of user profiles and renders them on an HTML page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response containing the user profiles list.
    """
    profiles_list = get_list_or_404(Profile)
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Render a user profile.

    This view retrieves a specific user's profile based on the username and
    renders it on an HTML page.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: A response containing the user's profile information.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
