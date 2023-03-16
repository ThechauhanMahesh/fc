import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(2992000)
    API_HASH = "235b12e862d71234ea222082052822fd"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "AQDuBr8AAYxUqz8VZUThvy4aD-XFpawuueugz-miE8taDna37YhK3xrGLM6RVEqssi2ZfAijRinFlmxPUVsu44HJniu9CFWuBSCS4WoPiiUv8hn016AtsW3wtL9Br1OmQTlOeL7bqAXVofTMYaKHfQjL_uRk2fogeMto6_z1IZ73x8sAbho9WwwWGvNO4l9l0hhphlIvHE8Z1gH_fTp4zij9VLNsOfb9d_xgJQXLNCLEANIKnuC56TO5P4W6H8Up4jJ812G6H2o6Wpbru2cM_izLFA0N_2FsSYV5vj-HBUtcz2dreH0qJiaYTMQ1pZERA1gsQPTbsC1Y0n8sL7scPpiajhNrMgAAAAFo_lRaAA"
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = []
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = []
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(3)
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
