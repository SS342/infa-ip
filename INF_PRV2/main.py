from flask import Flask, render_template
from flask import request as flask_request
from static.modules.DataBase import DataBase
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


DB = DataBase(config["DataBase"]["path"])
DB.CreateTableEmailPredReg()
DB.CreateTableDevBlog()
DB.CreateTableBugs()
DB.CreateTableCampSearch()
DB.close()

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Error? write to @allelleo"

@app.route('/', methods= ['POST' , 'GET'])
@app.route('/home', methods= ['POST' , 'GET'])
def home():
    if flask_request.method == 'POST':
        # print(f"Email : {flask_request.form['EmailPredReg']}")
        try:
            DB = DataBase(path=r"./static/db/main.db")
            DB.NewPredRegUser(flask_request.form['EmailPredReg'])
            return render_template('home.html')
        except:
            return render_template('home.html')
    else:
        return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Guides')
def Guides():
    return render_template('Guides.html')
    

@app.route('/dev-blog')
def devBlog():
    DB = DataBase(path=r"./static/db/main.db")
    posts = DB.GetDevBlog()
    DB.close()
    return render_template('dev-blog.html', posts=reversed(posts))
    

@app.route('/dev-blog/<int:id>')
def GetBlogPost(id):
    return render_template(f'dev-posts/{id}.html')


@app.route('/Bugs', methods = ['POST' , 'GET'])
def Bugs():
    if flask_request.method == 'POST':
        BugText = flask_request.form['bugs']
        print(f"BUG : [ {BugText} ]")
        try:
            DB = DataBase(path=r"./static/db/main.db")
            DB.NewBug(BugText)
            DB.close()
        except:
            pass
        return render_template('Bugs.html')
    else:
        return render_template('Bugs.html')
    

@app.route('/Camp')
def Camp():
    return render_template('Camp.html')
    

@app.route('/Camp/<string:server>/<string:_type_>')
def CampSearch(server, _type_):
    DB = DataBase(path=r"./static/db/main.db")
    camps = DB.SelectCamp(server, _type_)
    DB.close()
    return render_template('CampSearch.html', camps=camps)


@app.route('/Updates')
def Updates():
    return render_template('Updates.html')


@app.route('/Contact')
def Contact():
    return render_template('Contact.html')


@app.route('/guides/eat')
def guides_eat():
    return render_template('guide/eat.html')

__debug = config["Server"]["debug"]
__port = config["Server"]["port"]

if __name__ == '__main__':
    app.run(debug=__debug, port=__port)
