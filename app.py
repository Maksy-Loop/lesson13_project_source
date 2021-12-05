from flask import Flask, request, render_template, send_from_directory
from functions import search_unique_tag, is_tag

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = search_unique_tag("posts.json")
    return render_template('index.html', tags = tags)


@app.route("/tag")
def page_tag():
    tagname = request.args.get("tag")
    if tagname is None:
        return "Парень, ты не выбрал тег"
    else:
        posts_with_tag = is_tag("posts.json", tagname)
        return render_template('post_by_tag.html', posts_with_tag = posts_with_tag, tagname = tagname.title())


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

