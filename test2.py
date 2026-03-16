import os
from dotenv import load_dotenv

load_dotenv(".env")

print(os.environ.get("OPENAI_API_KEY"))
print(os.environ.get("GOOGLE_API_KEY"))
print(os.environ.get("GIT_ACCESS_TOKEN"))
print(os.environ.get("API_KEY"))
