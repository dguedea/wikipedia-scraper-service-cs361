from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from scrapeWiki import firstParagraph
from scrapeWiki import byId
from scrapeWiki import firstXParagraphs
from scrapeWiki import textUnderHTwo

app = Flask(__name__)
CORS(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'you'}


class FirstPara(Resource):
    def get(self, term, number):
        output = firstParagraph(term, number)
        return {
            'input': term,
            'output': output
        }


class ByHTMLID(Resource):
    def get(self, term, id):
        output = byId(term, id)
        return {
            'input': term,
            'output': output
        }


class FirstXPara(Resource):
    def get(self, term, number):
        output = firstXParagraphs(term, number)
        return {
            'input': term,
            'output': output
        }


class ParaUnderHTwo(Resource):
    def get(self, term, header, number):
        output = textUnderHTwo(term, header, number)
        return {
            'input' : term,
            'output' : output
        }


api.add_resource(HelloWorld, '/')
api.add_resource(FirstPara, '/firstpara/<term>/<int:number>')
api.add_resource(ByHTMLID, '/htmlid/<term>/<id>')
api.add_resource(FirstXPara, '/firstxpara/<term>/<int:number>')
api.add_resource(ParaUnderHTwo, '/paraunder/<term>/<header>/<int:number>')

if __name__ == '__main__':
    app.run(debug=True)
