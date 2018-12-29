from flask import render_template, request, Blueprint
from personalsite.models import Post

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return render_template('home.html')


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)