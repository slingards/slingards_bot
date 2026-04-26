from flask import Blueprint,render_template

paste_bp = Blueprint('paste_bp', __name__)
@paste_bp.route('/')
def paste():
    return render_template('index.html')

