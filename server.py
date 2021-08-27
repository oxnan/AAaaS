import re
import json
import random
import ascify
import requests, urllib
from bs4 import BeautifulSoup
from ddgapi import search
from quart import Quart, websocket, send_from_directory, request, render_template

def searchforimage(searchparameters):
    results = search(searchparameters)
    imageurl = results["results"][random.randint(0,len(results["results"])-1)]['image']
    return imageurl

app = Quart(__name__)

@app.route("/")
async def index():
    return await render_template("index.html", content=False)

@app.route("/api", methods=['POST', 'GET'])
async def echo():
    data = request.args.to_dict()
    try:
        searchterm = data['s']
        mode = data['mode']
        width = data['width']
        imageurl = searchforimage(searchterm)
        if mode == 'ascii':
            asciiart = ascify.runner(imageurl, width)
            return await render_template("index.html", content=True, asciiart=asciiart)
        elif mode == 'render':
            return f"""<img src='{imageurl}'></img>"""
    except Exception as e:
        print(e)
        return await send_from_directory("/", "failed.html")

if __name__ == "__main__":
    app.run()