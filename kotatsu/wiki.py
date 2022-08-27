# import urllib
# from slackbot.bot import listen_to

# @listen_to('(?:wiki)[\s ]+(.*)')
# def wiki(message, word):
#     url = "https://ja.wikipedia.org/wiki/" + urllib.parse.quote(word)
#     try:
#         f = urllib.request.urlopen(url)
#         f.close()
#         message.send(url)
#     except urllib.error.HTTPError:
#         message.send("NotFound : " + word)
