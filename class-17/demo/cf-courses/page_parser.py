from bs4 import BeautifulSoup


def parse(markup):
    soup = BeautifulSoup(markup, "html.parser")

    # beautiful soup often has a few ways
    # you can do the same thing

    courses = soup.select("article.calendar-event")
    # courses = soup.find_all('article', ["calendar-event"])
    # courses = soup('article', ["calendar-event"])

    course_info = "Course Info\n\n"

    # Note: with requests need to check if "Python" in course.h1.text:
    # this is needed at because of the "invisible" text coming through
    # with Playwright this isn't an issue

    for course in courses:
        if "Python" not in course.h1.text:
            continue

        # more examples of multiple styles
        # so don't be surprised if AI gives
        # you something a little different than expected

        course_info += course.h1.text + "\n"
        course_info += course.find("h2").get_text() + "\n"

        # sometimes you want to "reach up" to the parent element
        # I wonder how high you could reach?
        course_info += course.parent.find("h2").get_text() + "\n"

        # you can get parts not visible to user too
        course_info += course["id"] + "\n"

        course_info += "\n"

    return course_info
