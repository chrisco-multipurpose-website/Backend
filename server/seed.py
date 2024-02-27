from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import db, User, ChurchInfo, Service, Event, AboutUs, Department, Blog, SliderImage, TokenBlocklist, Role, PrayerRequest, Comment, user_roles
from sqlalchemy import text
from app import app

with app.app_context():
    User.query.delete()
    ChurchInfo.query.delete()
    Service.query.delete()
    Event.query.delete()
    AboutUs.query.delete()
    Department.query.delete()
    Blog.query.delete()
    SliderImage.query.delete()
    TokenBlocklist.query.delete()
    Role.query.delete()
    Comment.query.delete()

    # Execute a raw SQL query to delete all data from the user_roles table
    db.session.execute(text('DELETE FROM user_roles'))
    # Commit the transaction
    db.session.commit()

    users_data = [
        {"id": 1, "firstname": "John", "lastname": "Doe", "email": "johndoe@gmail.com", "password": generate_password_hash("john123"), "roles": ["superadmin"]},
        {"id": 2, "firstname": "Elisha", "lastname": "Kibet", "email": "elishakibet@gmail.com", "password": generate_password_hash("elisha123"), "roles": ["member"]},
        {"id": 3, "firstname": "Dan", "lastname": "Smith", "email": "dansmith@gmail.com", "password": generate_password_hash("dansmith123"), "roles": ["member"]},
        {"id": 4, "firstname": "Jane", "lastname": "Smith", "email": "janesmith@gmail.com", "password": generate_password_hash("janesmith123"), "roles": ["member"]},
        {"id": 5, "firstname": "Vera", "lastname": "Obiero", "email": "veraobiero@gmail.com", "password": generate_password_hash("vera123"), "roles": ["member"]},
    ]
    roles_data = [
        {"id": 1, "type": "member"},
        {"id": 2, "type": "admin"},
        {"id": 3, "type": "superadmin"},
    ]

    churchinfo_data = [
        {
            "id": 1, 
            "contact": "+254712345678", 
            "location": "Nairobi, Woodley, Ngonga Road", 
            "address": "Woodley, Kenya 00100", 
            "email": "chrisco.central@yahoo.com", 
            "website": "chriscocentralnrb.com", 
            "facebook_url": "https://www.facebook.com/chrisconairobi?mibextid=JRoKGi", 
            "instagram_url": "https://www.instagram.com/chrisconairobi", 
            "youtube_url": "https://www.youtube.com/@chrisconairobi", 
            "tiktok_url": "https://www.tiktok.com/@chrisconairobi", 
            "x_url": "https://twitter.com/chrisconairobi"}
    ]

    services_data = [
        {"id": 1, "name": "Service Service", "start_time" : "10:00 AM", "end_time": "12:00 PM", "service_type": "IN-PERSON & ONLINE SERVICE"},
        {"id": 2, "name": "Mid Week Service", "start_time" : "5.30 PM", "end_time": "7:00 PM", "service_type": "IN-PERSON"},
        {"id": 3, "name": "Overnight Service", "start_time" : "10:00PM", "end_time": "6:00 AM", "service_type": "IN-PERSON & ONLINE SERVICE"}
    ]

    events_data = [
        {
            "id": 1, 
            "event_img": "images/events/dinner.png", 
            "event_category": "Dinner", 
            "title": "Dinner Night", 
            "description": "Indulge in an evening of exquisite flavors and delightful company at our dinner night event", 
            "theme": "Connect Fellowship", 
            "scripture": "John 3:16", 
            "location": "Central Church", 
            "date": datetime.strptime("2024-02-22", "%Y-%m-%d").date(), 
            "start_time": "6:00 PM", 
            "end_time": "10:00 PM", 
            "event_host": "Catering Team"
        },
        {
            "id": 2, 
            "event_img": "images/events/youth.png", 
            "event_category": "Youth", 
            "title": "Youth Fellowship", 
            "description": "Engage with like-minded youths and build a strong spiritual foundation for a purpose life", 
            "theme": "Socializing, Fun and learning", 
            "scripture": "John 3:16", 
            "location": "Ruaka branch", 
            "date": datetime.strptime("2024-02-29", "%Y-%m-%d").date(), 
            "start_time": "10:00 AM", 
            "end_time": "4:00 PM", 
            "event_host": "Ruaka Youth"
        },
        {
            "id": 3, 
            "event_img": "images/events/outreach.png", 
            "event_category": "Outreach", 
            "title": "Community Outreach Programs", 
            "description": "Making positive impact on others by partcipating in other various community serice initiatives", 
            "theme": "Save a soul", 
            "scripture": "John 3:16", 
            "location": "Kitengela", 
            "date": datetime.strptime("2024-03-01", "%Y-%m-%d").date(), 
            "start_time": "2:00 PM", 
            "end_time": "5:00 PM ", 
            "event_host": "Central Church"
        }
    ]

    aboutus_data = [
        {
            "id": 1,
            "title": "Why Chrisco Central?",
            "description": "The Central Church is a congregation under the larger Christ’s co-Workers Fellowship (Chrisco) situated in Woodley in Nairobi, Kenya. The Central Church is headed by Presbyter Jeremiah Mugala and Pastor Rosemary Mugala together with other elder-ship. The Church aims at meeting the needs of the total man spiritually. Our dedicated team of elder-ship and volunteers work tirelessly to create warm and conducive environment for all.",
            "about_img": "images/about/about.png",
            "mission": "To equip believers through prayer, teaching God’s word, discipleship, evangelism, Christian living, tent-making so that they can be united, and attain the full knowledge of Christ in spiritual maturity",
            "vision": "To be a congregation of believers disciples under the five-fold ministry to fulfill the great commission of our Lord Jesus Christ.",
            "faith": "At Chrisco Central church, We offer a variety of services and programs to meet the spiritual needs of our congregation. Our Sunday services include uplifting music, inspiring sermons, and opportunities for personal growth and connection. We also have programs for children, youth, and adults throughout the week.",
            "faith_img": "images/about/faith.png",
            "word": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "word_img": "images/about/word.png",
            "trinity": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "trinity_img": "images/about/trinity.png",
            "baptism": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "baptism_img": "images/about/baptism.png",
            "church_slogan": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "purpose": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "history_desc": "",
        }
    ]

    departments_data = [
        {"id": 1, "title": "CHILDREN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/children.png"},
        {"id": 2, "title": "WORSHIP MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/worship.png"},
        {"id": 3, "title": "YOUTH MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/youth.png"},
        {"id": 4, "title": "MEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/men.png"},
        {"id": 5, "title": "WOMEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/women.png"},
        {"id": 6, "title": "INTERCESSORY MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/intercessory.png"},
        {"id": 7, "title": "EVANGELISM MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/evangelism.png"},
        {"id": 8, "title": "EDITORIAL MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/editorial.png"},
        {"id": 9, "title": "USHERS MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/ushering.png"},
        {"id": 10, "title": "FLOWERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/flowering.png"},
        {"id": 11, "title": "EQUIPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/equipment.png"},
        {"id": 12, "title": "CATERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/catering.png"},
        {"id": 13, "title": "CHURCH DEVELOPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "images/departments/development.png"},
    ]

    blogs_data = [
        {"id": 1, "title": "Teach to remember our days", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "images/blogs/blog1.png"},
        {"id": 2, "title": "The Spirit of God gives us power to do new things", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "images/blogs/blog2.png"},
        {"id": 3, "title": "What shall I render unto to the Lord for all His benefits towards me", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "images/blogs/blog3.png"},
        {"id": 4, "title": "Paul pursuit of the prize: Pressing towards the goal", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "images/blogs/blog4.png"},
        {"id": 5, "title": "When the winds howl and the waves crash around us", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "images/blogs/blog5.png"},
    ]

    sliders_data = [
        {"id": 1, "slider_img": "images/sliders/slider1.png"},
        {"id": 2, "slider_img": "images/sliders/slider2.png"},
        {"id": 3, "slider_img": "images/sliders/slider3.png"},
    ]


    print("Seeding roles data")
    for role_data in roles_data:
        role = Role(**role_data)
        db.session.add(role)
    db.session.commit()

    print("Seeding users data")
    for user_data in users_data:
        roles = user_data.pop("roles")
        user = User(**user_data)
        for role_type in roles:
            role = Role.query.filter_by(type=role_type).first()
            if role:
                user.roles.append(role)
            else:
                print(f"Role with type '{role_type}' not found for user {user['email']}")
        db.session.add(user)
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

    print("Seeding blogs data")
    for blog in blogs_data:
        data = Blog(**blog)
        db.session.add(data)
    db.session.commit()

    print("Seeding sliders data")
    for slider in sliders_data:
        data = SliderImage(**slider)
        db.session.add(data)
    db.session.commit()

    print("Seeding prayer requests data")
    requests = []
    for user in users_data:
        request = PrayerRequest(
            user_id = user["id"],
            request = "Prayer for peace, blessing, joy an unity amongst our nation",
        )

        db.session.add(request)
    db.session.commit()

    print("Seeding comments data")
    for user in users_data:
        for blog in blogs_data:  
            comment_data = {
                "user_id": user["id"],
                "blog_id": blog["id"],
                "comment": "The blog is awesome!"
                }
            comment = Comment(**comment_data)
            db.session.add(comment)
    db.session.commit()