from flask import Flask, request, render_template, send_from_directory, redirect
from functions import search_unique_tag, is_tag
import json

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


@app.route("/post", methods=["POST", "GET"])
def page_post_create():
    if request.method == "POST":
        content = request.form.get("content")
        picture = request.files["picture"]
        picture.save(f'uploads/images/{picture.filename}')
        picture_link = f'uploads/images/{picture.filename}'
        conv_dict = {
                "pic": picture_link,
                "content": content
            }
        with open('posts.json', "r") as f:
            list_date = json.load(f)

        list_date.append(conv_dict)

        with open('posts.json', "w") as f:
            json.dump(list_date, f, ensure_ascii=False, indent=4)

        return render_template('post_uploaded.html', **conv_dict)

    return render_template('post_form.html')


@app.route("/uploads/images/<path:path>")
def static_dir(path):
   return send_from_directory("uploads/images", path)


@app.errorhandler(500)
def page_not_found(e):
    return redirect("/post", code=302)


app.run()
