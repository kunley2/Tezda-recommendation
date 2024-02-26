from flask import Blueprint,render_template,request,redirect
# from .recommend import get_recommendation
import requests
import json
import os

views = Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
def index():

    return render_template('index.html')


# @views.route('products/',methods=['GET','POST'])
# def output():
#     """ this function is used to render a webpage for the output in the form from the index page
#             Parameters:
#                     user_id (str): the user id of the user to get recommendation
#     """
#     if request.method == "POST":
#         user_id = request.form.get('User-id')
#         response = get_recommendation(user_id)
        
#     return render_template('output.html', user_id=user_id, response=response)


@views.route('products/',methods=['GET','POST'])
def output():
    """ this function is used to render a webpage for the output in the form from the index page
            Parameters:
                    user_id (str): the user id of the uenvser to get recommendation
    """
    if request.method == "POST":
        user_id = request.form.get('User-id')
        url = os.getenv("BASE_URL")
        key = os.getenv("API_KEY")
        params = {
            "userId":user_id,
        }
        headers = {"x-api-key": key}
        response = requests.get(url,params=params,headers=headers).json()
        # print(response)
        # print(list(response))
        # print(response.json())
        print(response['data'])
        
    return render_template('output.html', user_id=user_id, response=response['data'])