import boto3
from dotenv import load_dotenv
import os
import pandas as pd
import json


load_dotenv()
link_df = pd.read_csv("./src/s3_bucket_links_1.csv", index_col="itemId")

client = boto3.client(
    'personalize-runtime',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name=os.getenv('region'),
)

def get_recommendation(user_id) -> dict:
    """ this function returns the recommeded product for a given user
            Parameters:
                    user_id (str): the user id of the user to get recommendation for

            Returns:
                    Recommendation (dict): a dictionary containing the recommended products id and their metadata
    """
    response = client.get_recommendations(
        campaignArn = os.getenv('arn'),
        userId = user_id,
        numResults = 10,
        metadataColumns = {
            "ITEMS":['childlabel',"genres"]
        }
    )
    recom_df = pd.DataFrame(response["itemList"])
    merged_df = pd.merge(recom_df,link_df,how='left',on='itemId')
    return json.loads(merged_df.to_json(orient='records'))
