#!/usr/bin/env python3

import ipdb

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db, Game, Device, Geedee, Developer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

# CORS(app)

api = Api(app)

class Games(Resource):
    
    def get(self):
        games = Game.query.all()
        response_body = []
        for game in games:
            response_body.append(game.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_game = Game(
                name=data.get('name'),
                image=data.get('image'),
                genre=data.get('genre'),
                online=data.get('online'),
                number_of_players=data.get('number_of_players'),
                description=data.get('description'),
                release_year=data.get('release_year'),
                developer_id=data.get('developer_id')
            )
            db.session.add(new_game)
            db.session.commit()
            response_body = new_game.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Games, '/games')

class GamesById(Resource):

    def get(self, id):
        game = Game.query.filter(Game.id == id).first()
        if not game:
            response_body = {'error': 'Game not found'}
            return make_response(jsonify(response_body), 404)
        response_body = game.to_dict()
        return make_response(jsonify(response_body), 200)

    def patch(self, id):
        game = Game.query.filter(Game.id == id).first()
        if not game:
            response_body = {'error': 'Game not found'}
            return make_response(jsonify(response_body), 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(game, key, data.get(key))
            db.session.commit()
            return make_response(jsonify(game.to_dict()), 202)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

    def delete(self, id):
        game = Game.query.filter(Game.id == id).first()
        if not game:
            response_body = {'error': 'Game not found'}
            return make_response(jsonify(response_body), 404)
        db.session.delete(game)
        db.session.commit()
        response_body = {}
        return make_response(jsonify(response_body), 204)

api.add_resource(GamesById, '/games/<int:id>')

class Developers(Resource):

    def get(self):
        developers = Developer.query.all()
        response_body = []
        for developer in developers:
            response_body.append(developer.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_developer = Developer(
                name = data.get('name'),
                logo = data.get('logo')
            )
            db.session.add(new_developer)
            db.session.commit()
            response_body = new_developer.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Developers, '/developers')

class Devices(Resource):

    def get(self):
        devices = Device.query.all()
        response_body = []
        for device in devices:
            response_body.append(device.to_dict())
        return make_response(jsonify(response_body), 200)

    def post(self):
        try:
            data = request.get_json()
            new_device = Device(
                name = data.get('name'),
                type = data.get('type'),
                image = data.get('image')
            )
            db.session.add(new_device)
            db.session.commit()
            response_body = new_device.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Devices, '/devices')

class DevicesById(Resource):

    def get(self, id):
        device = Device.query.filter(Device.id == id).first()
        if not device:
            response_body = {'error': 'Device not found'}
            return make_response(jsonify(response_body), 404)
        response_body = device.to_dict()
        return make_response(jsonify(response_body), 200)

    def patch(self, id):
        device = Device.query.filter(Device.id == id).first()
        if not device:
            response_body = {'error': 'Device not found'}
            return make_response(jsonify(response_body), 404)
        try:
            data = request.get_json()
            for key in data:
                setattr(device, key, data.get(key))
            db.session.commit()
            return make_response(jsonify(device.to_dict()), 202)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(DevicesById, '/devices/<int:id>')

class Geedees(Resource):

    def post(self):
        try:
            data = request.get_json()
            new_geedee = Geedee(
                game_id = data.get('game_id'),
                device_id = data.get('device_id')
            )
            db.session.add(new_geedee)
            db.session.commit()
            response_body = new_geedee.to_dict()
            return make_response(jsonify(response_body), 200)
        except ValueError:
            response_body = {'errors': ['validation errors']}
            return make_response(jsonify(response_body), 400)

api.add_resource(Geedees, '/geedees')

if __name__ == '__main__':
    app.run(port=7000, debug=True)