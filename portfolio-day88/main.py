import datetime
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


# WTForm
# class CreatePostForm(FlaskForm):
#     title = StringField("Blog Post Title", validators=[DataRequired()])
#     subtitle = StringField("Subtitle", validators=[DataRequired()])
#     author = StringField("Your Name", validators=[DataRequired()])
#     img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
#     body = CKEditorField("Blog Content", validators=[DataRequired()])
#     submit = SubmitField("Submit Post")


@app.route('/')
def get_all_cafes():
    cafes = Cafe.query.all()
    return render_template("index.html", all_cafes=cafes)


@app.route("/post/<int:index>")
def show_cafe(index):
    requested_cafe = Cafe.query.get(index)
    return render_template("post.html", cafe=requested_cafe)


# @app.route("/new-post", methods=["GET", "POST"])
# def add_new_cafe():
#     form = CreatePostForm()
#     if form.validate_on_submit():
#         new_post = Cafe(
#             title=form.title.data,
#             subtitle=form.subtitle.data,
#             date=datetime.date.today().strftime("%B %d, %Y"),
#             body=form.body.data,
#             author=form.author.data,
#             img_url=form.img_url.data,
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for("get_all_posts"))
#     return render_template("make-post.html", form=form)


# @app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
# def edit_cafe(post_id):
#     post = Cafes.query.get(post_id)
#     edit_form = CreatePostForm(
#         title=post.title,
#         subtitle=post.subtitle,
#         img_url=post.img_url,
#         author=post.author,
#         body=post.body
#     )
#     if edit_form.validate_on_submit():
#         post.title = edit_form.title.data
#         post.subtitle = edit_form.subtitle.data
#         post.img_url = edit_form.img_url.data
#         post.author = edit_form.author.data
#         post.body = edit_form.body.data
#         db.session.commit()
#         return redirect(url_for("show_post", index=post.id))
#     return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:cafe_id>")
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("get_all_cafes"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
