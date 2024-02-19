from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, ChurchInfo, Service, Event, AboutUs, Department, TokenBlocklist
from app import app

with app.app_context():
    User.query.delete()
    ChurchInfo.query.delete()
    Service.query.delete()
    Event.query.delete()
    AboutUs.query.delete()
    Department.query.delete()
    TokenBlocklist.query.delete()

    users_data = [
        {"id": 1, "firstname": "John", "lastname": "Doe", "email": "johndoe@gmail.com", "password": generate_password_hash("john123")},
        {"id": 2, "firstname": "Elisha", "lastname": "Kibet", "email": "elishakibet@gmail.com", "password": generate_password_hash("elisha123")},
        {"id": 3, "firstname": "Dan", "lastname": "Smith", "email": "dansmith@gmail.com", "password": generate_password_hash("dansmith123")},
        {"id": 4, "firstname": "Jane", "lastname": "Smith", "email": "janesmith@gmail.com", "password": generate_password_hash("janesmith123")},
        {"id": 5, "firstname": "Vera", "lastname": "Obiero", "email": "veraobiero@gmail.com", "password": generate_password_hash("vera123")},
    ]

    churchinfo_data = [
        {"id": 1, "contact": "+254712345678", "location": "Nairobi, Woodley, Ngonga Road", "facebook_url": "", "instagram_url": "", "youtube_url": "", "tiktok_url": "", "x_url": ""}
    ]

    services_data = [
        {"id": 1, "name": "Service Service", "start_time" : "10:00 AM", "end_time": "12:00 PM", "service_type": "IN-PERSON & ONLINE SERVICE"},
        {"id": 2, "name": "Mid Week Service", "start_time" : "5.30 PM", "end_time": "7:00 PM", "service_type": "IN-PERSON"},
        {"id": 3, "name": "Overnight Service", "start_time" : "10:00PM", "end_time": "6:00 AM", "service_type": "IN-PERSON & ONLINE SERVICE"}
    ]

    events_data = [
        {"id": 1, "title": "Dinner Night", "description": "Indulge in an evening of exquisite flavors and delightful company at our dinner night event", "image": ""},
        {"id": 2, "title": "Youth Fellowship", "description": "Engage with like-minded youths and build a strong spiritual foundation for a purpose life", "image": ""},
        {"id": 3, "title": "Community Outreach Programs", "description": "Making positive impact on others by partcipating in other various community serice initiatives", "image": ""}
    ]

    aboutus_data = [
        {
            "id": 1,
            "title": "Why Chrisco Central?",
            "description": "The Central Church is a congregation under the larger Christ’s co-Workers Fellowship (Chrisco) situated in Woodley in Nairobi, Kenya. The Central Church is headed by Presbyter Jeremiah Mugala and Pastor Rosemary Mugala together with other elder-ship. The Church aims at meeting the needs of the total man spiritually. Our dedicated team of elder-ship and volunteers work tirelessly to create warm and conducive environment for all.",
            "about_img": "",
            "mission": "To equip believers through prayer, teaching God’s word, discipleship, evangelism, Christian living, tent-making so that they can be united, and attain the full knowledge of Christ in spiritual maturity",
            "vision": "To be a congregation of believers disciples under the five-fold ministry to fulfill the great commission of our Lord Jesus Christ.",
            "faith": "At Chrisco Central church, We offer a variety of services and programs to meet the spiritual needs of our congregation. Our Sunday services include uplifting music, inspiring sermons, and opportunities for personal growth and connection. We also have programs for children, youth, and adults throughout the week.",
            "faith_img": "",
            "word": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "word_img": "",
            "trinity": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "trinity_img": "",
            "baptism": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "baptism_img": "",
            "church_slogan": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "purpose": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "history_desc": "",
        }
    ]

    departments_data = [
        {"id": 1, "title": "CHILDREN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 2, "title": "WORSHIP MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 3, "title": "YOUTH MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 4, "title": "MEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 5, "title": "WOMEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 6, "title": "INTERCESSORY MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 7, "title": "EVANGELISM MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 8, "title": "EDITORIAL MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 9, "title": "USHERS MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 10, "title": "FLOWERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 11, "title": "EQUIPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 12, "title": "CATERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
        {"id": 13, "title": "CHURCH DEVELOPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": ""},
    ]

    print("Seeding users data")
    for user in users_data:
        data = User(**user)
        db.session.add(data)
    db.session.commit()

    print("Seeding churchinfo data")
    for info in churchinfo_data:
        data = ChurchInfo(**info)
        db.session.add(data)
    db.session.commit()

    print("Seeding services data")
    for service in services_data:
        data = Service(**service)
        db.session.add(data)
    db.session.commit()

    print("Seeding events data")
    for event in events_data:
        data = Event(**event)
        db.session.add(data)
    db.session.commit()

    print("Seeding about_us data")
    for info in aboutus_data:
        data = AboutUs(**info)
        db.session.add(data)
    db.session.commit()

    print("Seeding departments data")
    for department in departments_data:
        data = Department(**department)
        db.session.add(data)
    db.session.commit()