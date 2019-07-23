import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    undefined = jinja2.StrictUndefined,
    autoescape = True,
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Okay I got this far")

class RecipesHandler(webapp2.RequestHandler):
    def get(self):
        recipes_template = the_jinja_env.get_template("recepies.html")
        self.response.write(recipes_template.render())

app = webapp2.WSGIApplication ([
    ("/", MainHandler),
    ("/recipes", RecipesHandler),
], debug=True)
