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
        print("Hello!")
        recipes_template = the_jinja_env.get_template("recepies.html")
        self.response.write(recipes_template.render())

    def post(self):
        apiKey = "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
        # url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
        userIngredients = []
        userIngredients.append(self.request.get("items"))
        print(userIngredients)
        template_vars = {

        }
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients=apples%2Cflour%2Csugar"
        response = urlfetch.fetch(url,method=1,headers={
              "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
              "X-RapidAPI-Key": "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
        })

        content = response.content
        as_json = json.loads(content)
        self.response.write(as_json[0]["title"])
        self.response.write(userIngredients)
        self.response.write(recipes_template.render())

class IngredientsHandler(webapp2.RequestHandler):
     def get(self):
         ingredients_template= the_jinja_env.get_template("ingredients.html")
         self.response.write(ingredients_template.render())

class RestrictionsHandler(webapp2.RequestHandler):
    def get(self):
        restrictions_template = the_jinja_env.get_template("restrictions.html")
        self.response.write(restrictions_template.render())

    def post(self):
        userstuff = self.request.get("items")
        self.response.write("checkpoint")
        print("howdy")
        print(self.request.POST.items())

app = webapp2.WSGIApplication ([
    ("/", MainHandler),
    ("/recipes", RecipesHandler),
    ("/ingredients", IngredientsHandler),
    ("/restrictions", RestrictionsHandler),
], debug=True)
