from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpResponse
from django.urls import path


def index(_request):
    with connection.cursor() as cursor:
        cursor.execute("select version()")
        version = cursor.fetchone()[0].split(" ")[0:2]
    return HttpResponse(
        f"fh-fixture django ok on {' '.join(version)}, auth users table rows: {User.objects.count()}",
        content_type="text/plain",
    )


urlpatterns = [path("", index)]
