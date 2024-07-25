import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
SESSION = os.getenv("SESSION", "BAGIzloAuVqc9pUpiCUzz-RhxrSuiTJGdFo4S0qAmxw3JclCDW3Caq4omKt2-cmlvRGZsthmvlaACB5ULFMlqQdpmI4CGHBygYHNnZmdqSEEpFjm8GUtQ3yOLXCJlHdINlP05dwGH1EDzWnTnDFhza_-lGBqa96Vvj1ggwZMHX9ea4M_U7qoKuNqc8N-vM6YVIREZTEAVSB3KZQwTmtS-m7zOwWg-AhV0hE1vNd9sTSxgrIK0Uilv03xoYtRAXRhd4VF6enxkQcfl4crgTrJO6ttUr2SjF5MsYYlfKVCshh1VS9ajcRTavAb1RbEcr62aeSB1w6z9bfVuDRLkRXxLECdmVmDxgAAAAF6nXj9AA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))

workdir = workdir or Path.cwd()
self.database = workdir / (self.name + self.FILE_EXTENSION)
call_py = PyTgCalls
