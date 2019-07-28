import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
import urllib
import json

userRestrictions = []
userIngredients = []

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

class IngredientsHandler(webapp2.RequestHandler):
     def get(self):
         ingredients_template= the_jinja_env.get_template("ingredients.html")
         self.response.write(ingredients_template.render())

class RestrictionsHandler(webapp2.RequestHandler):
    def get(self):
        restrictions_template = the_jinja_env.get_template("restrictions.html")
        self.response.write(restrictions_template.render())

    def post(self):
        global userIngredients
        restrictions_template = the_jinja_env.get_template("restrictions.html")
        self.response.write(restrictions_template.render())
        print("howdy")
        userIngredients = self.request.POST.items()
        print(userIngredients)

class RecipesHandler(webapp2.RequestHandler):
    def get(self):
        recipes_template = the_jinja_env.get_template("recepies.html")
        self.response.write(recipes_template.render())

    def post(self):
        global userRestrictions
        global userIngredients

        recipes_template = the_jinja_env.get_template("recepies.html")
        apiKey = "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
        userRestrictions = self.request.POST.items()

        apiKey = "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"

        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients?number=5&ranking=1&ignorePantry=false&ingredients="
        # url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"

        for x in userIngredients:
            for y in x:
                if y != "on":
                    url = url + str(y) + "%2C"

        response = urlfetch.fetch(url,method=1,headers={
              "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
              "X-RapidAPI-Key": "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
        })

        template_vars = {
            "options":[],
            "images":[],
            "percentages":[],
            "cookTimes": [],
            "directions":[],
            "missing":[],
        }

        content = response.content
        as_json = json.loads(content)

        print("work please")
        for x in  as_json:
            url2 = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"
            url2 = url2 + str(x["id"]) + "/information"

            response2 = urlfetch.fetch(url2, method=1, headers= {
                "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "40b69cdc47msh8fffdf56dc7aafdp13a859jsn7ee5daeb7842"
            })

            content2 = response2.content
            as_json2 = json.loads(content2)


            template_vars["options"].append(x["title"])
            template_vars["images"].append(x["image"])
            usedIngredients = len(x["usedIngredients"])
            missingIngredients = len(x["missedIngredients"])
            template_vars["percentages"].append(100 * float(usedIngredients)/float(missingIngredients))
            template_vars["cookTimes"].append(as_json2["readyInMinutes"])
            template_vars["directions"].append(as_json2["instructions"])
            w = len(x["missedIngredients"])-1
            list = []
            while w>0:
                template_vars["missing"].append(x["missedIngredients"][w]["name"])
                w-=1
            #Check this part
            i = 0
            while i < len(as_json2["extendedIngredients"]):
                for y in userRestrictions:
                    if (y!="on" and y== as_json2["extendedIngredients"][i]["name"]) or (y!="on" and y=="vegetarian" and (as_json2["vegetarian"]==false)):
                        index = template_vars["options"].index(y)
                        template_vars["options"].remove(y)
                        template_vars["images"].remove(template_vars["images"][index])
                        template_vars["percentages"].remove(template_vars["percentages"][index])
                        template_vars["cookTimes"].remove(template_vars["cookTimes"][index])
                        template_vars["directions"].remove(template_vars["directions"][index])
                i+=1

        self.response.write(recipes_template.render(template_vars))

class ChoosenRecipeHandler(webapp2.RequestHandler):
    def get(self):
        theReceipe_template = the_jinja_env.get_template("choosenRecipe.html")
        template_varsAgain = {
            "title":"",
            "content":"",
            "ingredients":"",
            "image":"",
            "missing":"",
        }
        template_varsAgain["title"] = self.request.get("title")
        template_varsAgain["content"] = self.request.get("content")
        template_varsAgain["ingredients"] = self.request.get("ingredients")
        template_varsAgain["image"]=self.request.get("image")
        template_varsAgain["missing"]=self.request.get("missing")
        self.response.write(theReceipe_template.render(template_varsAgain))
        #self.response.write(theReceipe_template.render(template_varsAgain))


app = webapp2.WSGIApplication ([
    ("/", MainHandler),
    ("/recipes", RecipesHandler),
    ("/ingredients", IngredientsHandler),
    ("/restrictions", RestrictionsHandler),
    ("/choosenrecipe", ChoosenRecipeHandler),
], debug=True)
