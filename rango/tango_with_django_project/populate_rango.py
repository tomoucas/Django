import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def Populate():
    python_pages = [
        {"title":"Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views":64, "likes":32},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views":32, "likes":16},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views":16, "likes":8}]

    django_pages = [
        {"title":"Official Django Tutorial",
        "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views":64, "likes":32},
        {"title":"Django Rocks",
        "url":"http://www.djangorocks.com/",
         "views":32, "likes":16},
        {"title":"How to Tango with Django",
        "url":"http://www.tangowithdjango.com/",
         "views":16, "likes":8} ]

    other_pages = [
        {"title": "Bottle",
        "url":"http://bottlepy.org/docs/dev/",
         "views":32, "likes":16},
        {"title": "Flask",
        "url": "http://flask.pocoo.org",
         "views":16, "likes":8}]

    categories = {
        "Python": {"name":"Python", "pages": python_pages, "views":128, "likes":64},
        "Django": {"name":"Django","pages": django_pages, "views":64, "likes":32},
        "Other Frameworks": {"name":"Other Frameworks", "pages": other_pages, "views":32, "likes":16}}

    def add_page(data, category):
        print(data)
        page = Page.objects.get_or_create(category=category,title=data["title"])[0]
        page.url=data["url"]
        page.likes=data["likes"]
        page.views=data["views"]
        page.save()
        return page

    def add_category(data):
        category = Category.objects.get_or_create(name=data["name"])[0]
        category.views = data["views"]
        category.likes = data["likes"]
        category.save()
        return category

    for category, category_data in categories.items():
        category = add_category(category_data)
        for page in category_data["pages"]:
            add_page(page, category)

    for category in Category.objects.all():
        for page in Page.objects.all():
            print("- {0} - {1}".format(str(category), str(page)))


if __name__ == '__main__':
    print("Starting population script")
    Populate()