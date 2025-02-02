'''
1. I created the project and installed django in vertual environment 
2. I connected my project to github
3. For template I made these changes: 

> (.venv) > mkdir templates

> # django_project/settings.py
TEMPLATES = [{"DIRS": [BASE_DIR / "templates"], # new},]

> # pages/views.py
from django.views.generic import TemplateView
class HomePageView(TemplateView):
template_name = "home.html"

> # django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
path("admin/", admin.site.urls),
path("", include("pages.urls")), # new
]

> # pages/urls.py
from django.urls import path
from .views import HomePageView
urlpatterns = [
path("", HomePageView.as_view(), name="home"),
path("about/", AboutPageView.as_view(), name="about"), # new
]

4. Commit to github:

'''