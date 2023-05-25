from .models import Genre


def nav_context(request):
    return {
        "genres": Genre.objects.order_by("id").all()
    }
