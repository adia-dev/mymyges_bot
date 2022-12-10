import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def set_token(user_id: str, token: str):
    """
    Saves the provided token in Redis for the specified user.

    Args:
        user_id (str): The ID of the user to save the token for.
        token (str): The token to save in Redis.
    """
    redis_client.set(user_id, token)


def get_token(user_id: str) -> str:
    """
    Retrieves the token saved in Redis for the specified user.

    Args:
        user_id (str): The ID of the user to retrieve the token for.

    Returns:
        str: The token saved in Redis for the user.
    """
    if redis_client.exists(user_id):
        return redis_client.get(user_id).decode("utf-8")
    else:
        return None


def delete_token(user_id: str):
    """
    Deletes the token saved in Redis for the specified user.

    Args:
        user_id (str): The ID of the user to delete the token for.
    """
    redis_client.delete(user_id)
