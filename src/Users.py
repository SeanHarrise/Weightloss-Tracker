import boto3
import logging
from botocore.exceptions import ClientError


class Users:
    """Encapsulates an Amazon DynamoDB table of app users"""
        
    def __init__(self, dyn_resource):
        """
        :param dyn_resource: A Boto3 DynamoDB resource.
        """
        self.dyn_resource = dyn_resource
        # The table variable is set during the scenario in the call to
        # 'exists' if the table exists. Otherwise, it is set by 'create_table'.
        self.table = None

    def get_user(self, user_id):
        """
        Gets movie data from the table for a specific movie.

        :param user_id: The user_if of the user
        :return: The data about the requested user
        """
        try:
            response = self.table.get_item(Key={"user_id": user_id})
        except ClientError as err:
            print(
                   "Couldn't get movie %s from table %s. Here's why: %s: %s",
                   user_id,
                   self.table.name,
                   err.response["Error"]["Code"],
                   err.response["Error"]["Message"]
                 )
            raise
        else:
            return response["Item"]