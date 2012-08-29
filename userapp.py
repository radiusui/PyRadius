#!/usr/bin/env python
#coding:utf-8

from utils import route_app
from settings import config
from utils import render
import web

app  = route_app()

@app.route("")
class routeto():
    def GET(self):
        raise web.seeother("/user/",absolute=True)

@app.route("/")
class index():
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        return render("user.html") 