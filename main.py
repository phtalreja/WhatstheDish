import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import urllib
import json

the_jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    undefined = jinja2.StrictUndefined,
    autoescape = True,
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template("home.html")
        self.response.write(home_template.render())

class RecipesHandler(webapp2.RequestHandler):
    def get(self):
        recipes_template = the_jinja_env.get_template("recepies.html")
        apiKey = "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
        # url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients=apples%2Cflour%2Csugar"
        response = urlfetch.fetch(url,method=1,headers={
              "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
              "X-RapidAPI-Key": "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"

        })
        content = response.content
        self.response.write(recipes_template.render())

class IngredientsHandler(webapp2.RequestHandler):
     def get(self):
         ingredients_template= the_jinja_env.get_template("ingredients.html")
         self.response.write(ingredients_template.render())

app = webapp2.WSGIApplication ([
    ("/", MainHandler),
    ("/recipes", RecipesHandler),
    ("/ingredients", IngredientsHandler),
], debug=True)
