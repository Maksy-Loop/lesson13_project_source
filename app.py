from flask import Flask, request, render_template, send_from_directory, redirect, abort
from functions import search_unique_tag, is_tag, add_value
import json

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    tags = search_unique_tag(POST_PATH)
    return render_template('index.html', tags = tags)


@app.route("/tag")
def page_tag():
    tagname = request.args.get("tag")
    if tagname is None:
        abort(404)
    else:
        posts_with_tag = is_tag("posts.json", tagname)
        return render_template('post_by_tag.html', posts_with_tag = posts_with_tag, tagname = tagname.title())


@app.route("/post", methods=["POST", "GET"])
def page_post_create():
    if request.method == "POST":
        content = request.form.get("content")
        picture = request.files["picture"]

        if content and picture:
            picture.save(f'{UPLOAD_FOLDER}/{picture.filename}')
            picture_link = f'uploads/{picture.filename}'
            conv_dict = {
                    "pic": picture_link,
                    "content": content
                }
            add_value(conv_dict, POST_PATH)
            return render_template('post_uploaded.html', **conv_dict)
        else:
            abort(400)

    return render_template('post_form.html')

@app.route("/uploads/<path:path>")
def static_dir(path):
   return send_from_directory(UPLOAD_FOLDER, path)


app.run()
