#!/usr/bin/env python3

from app import app
from models import db, Game, Device, Developer, Geedee

with app.app_context():
    
    Game.query.delete()
    Device.query.delete()
    Developer.query.delete()
    Geedee.query.delete()

    developers = []
    developers.append(Developer(name='Activision', logo='https://banner2.cleanpng.com/20180525/wui/kisspng-prototype-activision-blizzard-video-game-skylander-5b07b7a1f07547.6335945515272324179849.jpg'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    developers.append(Developer(name='Bandi Namco Entertainment', logo='https://companieslogo.com/img/orig/7832.T-afbe2170.png?t=1643617765'))
    

    games = []
    games.append(Game(name='Call of Duty: Modern Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Modern Wrfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: ModernWarfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Moden Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Morn Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Modrn Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Modern rfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of Duty: Modern arfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call o Duty: Mrn Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call f Duty: Modern Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Call of uy: Modern Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))
    games.append(Game(name='Cal of Duty: Modern Warfare 3', release_year=2011, image='https://cdn.europosters.eu/image/1300/posters/call-of-duty-mw3-cover-i11163.jpg', genre='Shooter', online=True, number_of_players=4, description='This is a first-person shooter in which players assume the role of military operatives tasked with thwarting the plans of a terrorist leader. Players complete mission objectives and engage in battles that take place in modern-day locations across the globe.', developer_id=1))

    devices = []
    devices.append(Device(name='PlayStation', type='Console', image='https://icon2.cleanpng.com/20180327/swq/kisspng-one-crash-bandicoot-playstation-2-playstation-3-1-5abb04558b5c91.5310581515222057815708.jpg'))
    devices.append(Device(name='PlayStation 2', type='Console', image='https://p7.hiclipart.com/preview/466/253/287/playstation-2-playstation-3-playstation-4-video-game-consoles-sony-playstation.jpg'))
    devices.append(Device(name='PlayStation 3', type='Console', image='https://www.vhv.rs/dpng/d/546-5462815_playstation-3-hd-hd-png-download.png'))
    devices.append(Device(name='PlayStation 4', type='Console', image='https://p7.hiclipart.com/preview/305/624/859/twisted-metal-black-playstation-2-playstation-4-playstation-3-others.jpg'))
    devices.append(Device(name='PlayStation 5', type='Console', image='https://image.pngaaa.com/542/3365542-middle.png'))
    devices.append(Device(name='Nintendo 64', type='Console', image='https://p7.hiclipart.com/preview/35/125/113/nintendo-64-controller-video-game-consoles-game-controllers-nintendo.jpg'))
    devices.append(Device(name='Nintendo GameCube', type='Console', image='https://p7.hiclipart.com/preview/570/622/437/gamecube-wii-playstation-2-video-game-consoles-nintendo-video-games.jpg'))
    devices.append(Device(name='Nintendo Wii', type='Console', image='https://www.vhv.rs/dpng/d/179-1797124_nintendo-wii-hd-png-download.png'))
    devices.append(Device(name='Nintendo Wii U', type='Console', image='https://p7.hiclipart.com/preview/456/1011/636/wii-u-wii-sports-super-mario-galaxy-nintendo-nintendo.jpg'))
    devices.append(Device(name='Nintendo Switch', type='Console', image='https://www.vhv.rs/dpng/d/417-4176077_nintendo-switch-png-image-nintendo-switch-png-transparent.png'))
    devices.append(Device(name='Xbox', type='Console', image='https://image.pngaaa.com/402/2928402-middle.png'))
    devices.append(Device(name='Xbox 360', type='Console', image='https://www.pngfind.com/pngs/m/259-2591374_xbox-360-png-xbox-360-white-png-transparent.png'))
    devices.append(Device(name='Xbox One', type='Console', image='https://banner2.cleanpng.com/20180411/brq/kisspng-kinect-xbox-360-black-playstation-3-xbox-one-console-5acddec6821d23.205181881523441350533.jpg'))
    devices.append(Device(name='Xbox Series X', type='Console', image='https://www.citypng.com/public/uploads/preview/-11599586928svl1wf1mjz.png?v=2023060709'))
    devices.append(Device(name='Nintendo Gameboy Advance', type='Handheld', image='https://www.vhv.rs/dpng/d/430-4306675_transparent-gameboy-color-png-gameboy-advance-sp-png.png'))
    devices.append(Device(name='Nintendo DS', type='Handheld', image='https://www.pngitem.com/pimgs/m/299-2998932_nintendo-double-diamond-anniversary-retrospective-part-nintendo-ds.png'))
    devices.append(Device(name='Nintendo 3DS', type='Handheld', image='https://p7.hiclipart.com/preview/100/827/776/new-nintendo-3ds-handheld-game-console-nintendo-ds-nintendo.jpg'))
    devices.append(Device(name='PlayStation Portable', type='Handheld', image='https://cdn.imgbin.com/5/23/3/imgbin-playstation-2-psp-e1000-playstation-portable-handheld-game-console-sony-qMSJy6MWVqq9FyYZMvEbazdaJ.jpg'))
    devices.append(Device(name='Gaming PC', type='PC', image='https://www.vhv.rs/dpng/d/134-1346701_college-tour-element-z-gaming-pc-transparent-background.png'))
    

    geedees = []
    geedees.append(Geedee(game_id=1, device_id=3))
    geedees.append(Geedee(game_id=5, device_id=3))
    geedees.append(Geedee(game_id=2, device_id=3))
    geedees.append(Geedee(game_id=3, device_id=3))
    geedees.append(Geedee(game_id=1, device_id=8))
    geedees.append(Geedee(game_id=1, device_id=12))
    geedees.append(Geedee(game_id=1, device_id=19))

    db.session.add_all(developers)
    db.session.add_all(games)
    db.session.add_all(devices)
    db.session.add_all(geedees)
    db.session.commit()
    print("🌱 Successfully seeded! 🌱")