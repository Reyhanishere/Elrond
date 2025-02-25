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
4. Commit changes to github:                       
     1️⃣ Check what changed (optional but useful)
    Before committing, you can check what files were modified:
    (.venv) git status

    2️⃣ Stage the changes
    Add all modified files to the commit:
    (.venv) git add .

    3️⃣ Commit the changes
    Commit with a meaningful message:
    (.venv) git commit -m "Describe your changes here"
   
    4️⃣ Push the changes to GitHub
    Send your changes to GitHub:
    (.venv) git push origin main
    (Replace main with your actual branch name if needed.)

5. I made base.html in templates folder:
    <!-- templates/base.html -->
    <header>
    <a href="{% url 'home' %}">Home</a> |
    <a href="{% url 'about' %}">About</a>
    </header>
    {% block content %} {% endblock content %}
    > then I chansed my other html files like this:
    <!-- templates/home.html -->
    {% extends "base.html" %}
    {% block content %}
    <h1>Homepage</h1>
    {% endblock content %}
6. I learned about test but didn't use them and added these codes to test.py:
    *test.py
    from django.test import SimpleTestCase
    from django.urls import reverse

    class HomepageTests(SimpleTestCase):
        def test_url_exists_at_correct_location(self):
            response = self.client.get("/")
            self.assertEqual(response.status_code, 200)
        def test_url_available_by_name(self):
            response = self.client.get(reverse("home"))
            self.assertEqual(response.status_code, 200)
        def test_template_name_correct(self): # new
            response = self.client.get(reverse("home"))
            self.assertTemplateUsed(response, "home.html")
        def test_template_content(self): # new
            response = self.client.get(reverse("home"))
            self.assertContains(response, "<h1>Homepage</h1>")
    
    class AboutpageTests(SimpleTestCase):
        def test_url_exists_at_correct_location(self):
            response = self.client.get("/about/")
            self.assertEqual(response.status_code, 200)
        def test_url_available_by_name(self):
            response = self.client.get(reverse("about"))
            self.assertEqual(response.status_code, 200)
        def test_template_name_correct(self): # new
            response = self.client.get(reverse("about"))
            self.assertTemplateUsed(response, "about.html")
        def test_template_content(self): # new
            response = self.client.get(reverse("about"))
            self.assertContains(response, "<h1>About page</h1>")
    *Shell:
    (.venv) > python manage.py test
7. Deploy our code (I couldn't log in to heroku,this step got postponed

* Helped by DeepSeek > made a shell of a web!
8. 
'''