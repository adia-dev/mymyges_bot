import asyncio
import os


def save_data(path, filename: str, data: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

    filepath = os.path.join(path, filename)

    with open(filepath, "w") as file:
        file.write(data)
