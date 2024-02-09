from flask import Blueprint,render_template,request,redirect
from .recommend import get_recommendation

views = Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
def index():

    return render_template('index.html')


@views.route('products/',methods=['GET','POST'])
def output():
    # print(request.method)
    if request.method == "POST":
        user_id = request.form.get('User-id')
        response = get_recommendation(user_id)
        print(response)
        
    return render_template('output.html', user_id=user_id, response=response)