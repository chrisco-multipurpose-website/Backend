from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import db, User, ChurchInfo, Service, Event, AboutUs, Department, Blog, SliderImage, TokenBlocklist, PrayerRequest, Comment, Inquiry, Subscription
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
    PrayerRequest.query.delete()
    # Role.query.delete()
    Comment.query.delete()
    Inquiry.query.delete()
    Subscription.query.delete()

    # # Execute a raw SQL query to delete all data from the user_roles table
    # db.session.execute(text('DELETE FROM user_roles'))
    # # Commit the transaction
    # db.session.commit()

    users_data = [
        {"id": 1, "firstname": "John", "lastname": "Doe", "email": "johndoe@gmail.com", "password": generate_password_hash("john123"), "role": "superadmin"},
        {"id": 2, "firstname": "Elisha", "lastname": "Kibet", "email": "elishakibet@gmail.com", "password": generate_password_hash("elisha123"), "role": "admin"},
        {"id": 3, "firstname": "Dan", "lastname": "Smith", "email": "dansmith@gmail.com", "password": generate_password_hash("dansmith123"), "role": "member"},
        {"id": 4, "firstname": "Jane", "lastname": "Smith", "email": "janesmith@gmail.com", "password": generate_password_hash("janesmith123"), "role": "member"},
        {"id": 5, "firstname": "Vera", "lastname": "Obiero", "email": "veraobiero@gmail.com", "password": generate_password_hash("vera123"), "role": "member"},
    ]
    # roles_data = [
    #     {"id": 1, "type": "member"},
    #     {"id": 2, "type": "admin"},
    #     {"id": 3, "type": "superadmin"},
    # ]

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
            "event_img": "https://lh3.googleusercontent.com/pw/AP1GczM90vQz88zrfi7NoN6AZteH1bmUJNV5kpO9niTGy9kBGSph_H8WDTQne8UiCv4tOAAM6Y3JBdbtiuFXF5l2-JJFMj_0xnRaTGnvv6N4YuS3FqZoUg=w2400", 
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
            "event_img": "https://lh3.googleusercontent.com/pw/AP1GczNg2brGt_bNs7pVmDRH2uoR4BxR_WbnWwHwKfnKW1N3UFohsrE5giNpuxQBlXmR0VtB7PtOUHXcmMS7TkMKEy6RHFHjTGfxIIYdEf6mpPBmmbdrgQ=w2400", 
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
            "event_img": "https://lh3.googleusercontent.com/pw/AP1GczP0ftzEtUN33YQ2FIy_XO2mGZqCD2SeL45bUkdW_2E1tbnqkGxLZEWbcJ_MOEF2eAyOD63EZQpHc8PXBEYtqOcpOO3rSqN1EmV7TOceVRJxkjmGWA=w2400", 
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
        {"id": 1, "title": "CHILDREN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczNi2oztzL6CuP1PyVJRh9WcKQrxgckmU7VJHTzh2MnNuTQBIpfAzFRbjyWQPXORpHFRIGNL-UAIlV1eETkIE_LymN_V9pSCcdA4eJuQBdSEOSiwYQ=w2400"},
        {"id": 2, "title": "WORSHIP MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczNjuzZXNeht1TQvfkmvYh1Bey6Smw139Y47t6wLTPbMt3Fy4PoRGpcSi0xVvaNdpH0BDQk2mTA5Nvo1JehAz9FFKhUhN2w5hQJsgjSg-g25sPrhXA=w2400"},
        {"id": 3, "title": "YOUTH MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczNCOjWZt2K5euoH4te29S-bhlQa1KPx-raZ61x0o4tj3JqiDRoBrItNni0lQcsyvROW1lBT4pkXBm3zYRDT_dl9EY7G7NToGSvqjtj-Ghvflv06Dw=w2400"},
        {"id": 4, "title": "MEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczPQ3ZZeEEuGESBi-di9GY65EHcc1fsndzUBvTzSETlkSSQfSqDty7q0xdMkPpipY6BTkohs2WOIKfKcMkdmJ6-jvqdlsmUtI06gWpUwGlMNSezIRw=w2400"},
        {"id": 5, "title": "WOMEN'S MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczPO3LUXgI4SoFR3QZ08XhgnVi6lxAt_-iRlM7Zn2Xanci8XOQ383_kK4SOtzRObOLckQZu97JCe52jf-H6u5uLGw514USvu5ItasiNoHXdFeF6eZg=w2400"},
        {"id": 6, "title": "INTERCESSORY MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczMxd9JcjEpWogzkphm_eJ4SEZHuRZ57vxw8P06g6ucv08GSpXm3Evuj2L51gszO6oh9bweCP2GkWEK4qtaS0rHrA6v2WQY9hvIYoEz62KmHDFjSmA=w2400"},
        {"id": 7, "title": "EVANGELISM MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczNtqevLsvhwzCRYs5MyDyZv3SpiolXDvPsPK_x1-9Nhikx-UL3xO1kF-iY9BZw8VoGt2lFyrSWG2Ffn0uaBv1zKzr4to1OIbnJXYVP7FXl2wKfTNg=w2400"},
        {"id": 8, "title": "EDITORIAL MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczO9GKbM1LrXRhlTzmfAGoCcJf6FMF1oMS-5nrCdTWHvA-X0Y7E2vE3o_xCAr9lFIrzUVENOFTv9TarHmWM5YWRY7qqA_iX0wY6j7IlJcngWt0AQ3w=w2400"},
        {"id": 9, "title": "USHERS MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczOZJJ486XGRMDNDQ9Xdpwld7WUnASFMM1txXjk9MUGwIVSW3Pb1ugHy9kEsgo2EiNIo1eYr0ktWbnJa7lAR4BP4MxuZGFmyErMw54Hvhz4v1s2mvw=w2400"},
        {"id": 10, "title": "FLOWERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczOUWbRxNsDi4vdAA-VE23-Hd7EFPI9-bM3wS0RkTu_7x7TVtV6avO8iOVloUeeN26gXuEhgXNROQwclyjIoip8NKVaFC2XFUmKjk9ngTA85LcvwHw=w2400"},
        {"id": 11, "title": "EQUIPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczMsQ-QFYgNHAtA-orpHYFL5uO--6AcIn_C5qwihDXCvJD8gQPeI8BrtUM3qH2ZaVD0j0XMW3gaTJO_Y1-ygOMik0utVzqGf5qUtKoCfxNbPOzNyig=w2400"},
        {"id": 12, "title": "CATERING MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczOD3iMBC8dMtBcVyAmUHJGxQOG5aBQ6otetd_xon9wf-B1eP89Nh79_Kz799yrjZQUQPnD-AEiRdF10zJX8RO6u_pvpyKITvuNLnXASTXqIaQqR7g=w2400"},
        {"id": 13, "title": "CHURCH DEVELOPMENT MINISTRY", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "department_img": "https://lh3.googleusercontent.com/pw/AP1GczNBmdm-HytWnmYIsYfQ3YTn4mpUBEbGf3oKFBiNm5GD1RJjkBJXi0939QVeyXwD5J76dtrrp_cQP8og-iFUr6tKXzP_HevOtUqnUNZw4NybjVMBHA=w2400"},
    ]

    blogs_data = [
        {"id": 1, "title": "Teach to remember our days", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczNR_cU-twN3cJ0N2bhEST6ae5DNb_-fRw14dM8smmoLPpEX3kMlUzkO27HqUEpIkKCCGnXp88nPID3VjSgAkuwB92qobGL1-pCERWYUTo5fAr8MNg=w2400"},
        {"id": 2, "title": "The Spirit of God gives us power to do new things", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczPlvnommVZf1P-3nHAlgbCCLF1X9b4_n8K8m33dVOjNWNZ4ZDxFFAumZDftezsYHG71olCwpAxl8FkXN0EISFQU-WJbO6ppyBaYkDp6uvJrRn92IQ=w2400"},
        {"id": 3, "title": "What shall I render unto to the Lord for all His benefits towards me", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczOtyAi7X2-R5y1U4XlT_BQJhg5fAVwqBGkp-I5S0H_VEt5JsgW5K0vtcBfOZ3-2lONw1mplBCwJJdy6JHMyr4Qa3feuG1vicRofjJ-eaEoNcD3X5g=w2400"},
        {"id": 4, "title": "Paul pursuit of the prize: Pressing towards the goal", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczPGKg59zsgPLDv12_riXKlfPflGAz4-YU8G6YJCDIRq3u57WA8BF9-WrkKijSk6FcSZkYBgcAWEsfrq1l2rQSCOurmTSQt6P5QeLx6O80KLCa7CEQ=w2400"},
        {"id": 5, "title": "When the winds howl and the waves crash around us", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore", "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczNhzcahl8n5w8gHaNoxYB0Lq-Mqsnf_KRBIhvd3_xNa6OtZQNuKIqCRZyoMEqsyMo3C31qq9Gwk4mGO3-0tB0reyBCYnwwyIsWpFF4Zxy5gOO-H0Q=w2400"},
    ]

    sliders_data = [
        {"id": 1, "slider_img": "images/sliders/slider1.png"},
        {"id": 2, "slider_img": "images/sliders/slider2.png"},
        {"id": 3, "slider_img": "images/sliders/slider3.png"},
    ]

    subscriptions_data = [
        {"id": 1, "email": "alice@gmail.com"},
        {"id": 2, "email": "titus@gmail.com"},
        {"id": 3, "email": "emmanuel@gmail.com"}
    ]

    inquiries_data = [
        {"id": 1, "name": "Alice Kyalo", "email": "alice@gmail.com", "inquiry": "Where is your church located at?"},
        {"id": 2, "name": "Titus Kip", "email": "titus@gmail.com", "inquiry": "Want to contact church pastor"},
        {"id": 3, "name": "Emmanuel Kip", "email": "emmanuel@gmail.com", "inquiry": "Want to join the church choir"}
    ]
    # print("Seeding roles data")
    # for role_data in roles_data:
    #     role = Role(**role_data)
    #     db.session.add(role)
    # db.session.commit()

    print("Seeding users data")
    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)
    db.session.commit()

    # for user_data in users_data:
    #     roles = user_data.pop("roles")
    #     user = User(**user_data)
    #     for role_type in roles:
    #         role = Role.query.filter_by(type=role_type).first()
    #         if role:
    #             user.roles.append(role)
    #         else:
    #             print(f"Role with type '{role_type}' not found for user {user['email']}")
    #     db.session.add(user)
    # db.session.commit()

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

    print("Seeding subscriptions data")
    for subscription in subscriptions_data:
        data = Subscription(**subscription)
        db.session.add(data)
    db.session.commit()

    print("Seeding inquiries data")
    for inquiry in inquiries_data:
        data = Inquiry(**inquiry)
        db.session.add(data)
    db.session.commit()