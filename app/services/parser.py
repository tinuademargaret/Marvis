from app.services.stt import transcribe_streaming

import re
"""
keyword = 'Marvis open bible 
           Marvis Search for
           Marvis next/previous/nth slide'
"""


def parser():
    q = transcribe_streaming()
    transcript = q.get()
    command = re.search('Marvis', transcript)
    return command









