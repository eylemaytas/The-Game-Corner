#!/usr/bin/env python3

from app import app
from models import db, Game, Device, Developer, Geedee

with app.app_context():
    
    Game.query.delete()
    Device.query.delete()
    Developer.query.delete()
    Geedee.query.delete()

    developers = []
    developers.append(Developer(name='Freddie', logo='poop'))
    developers.append(Developer(name='Anthony', logo='apples'))
    developers.append(Developer(name='Eddie', logo='Steve'))
    developers.append(Developer(name='Eylem', logo='sunshine'))

    games = []
    games.append(Game(name='Call of Duty', image='https://static1.srcdn.com/wordpress/wp-content/uploads/2020/12/Call-Of-Duty-Game-Covers.jpg', genre='Shooter', online=True, number_of_players=2, description='The original first-person shooter.', developer_id=1))
    games.append(Game(name='Battlefield', image='https://static1.srcdn.com/wordpress/wp-content/uploads/2020/12/Call-Of-Duty-Game-Covers.jpg', genre='Shooter', online=True, number_of_players=2, description='The other original first-person shooter.', developer_id=2))
    games.append(Game(name='The Last of Us', image='https://static1.srcdn.com/wordpress/wp-content/uploads/2020/12/Call-Of-Duty-Game-Covers.jpg', genre='Action', online=True, number_of_players=4, description='Survive the zombie apocolypse in The Last of Us', developer_id=1))

    devices = []
    devices.append(Device(name='PlayStation', type='Console', image='poop'))
    devices.append(Device(name='Xbox', type='Console', image='poop'))
    devices.append(Device(name='Nintendo DS', type='Handheld', image='poop'))

    geedees = []
    geedees.append(Geedee(game_id=1, device_id=1))
    geedees.append(Geedee(game_id=1, device_id=2))
    geedees.append(Geedee(game_id=2, device_id=1))

    # db.session.add_all(developers)
    # db.session.add_all(games)
    # db.session.add_all(devices)
    # db.session.add_all(geedees)
    db.session.commit()
    print("🌱 Successfully seeded! 🌱")
