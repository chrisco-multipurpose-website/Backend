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
            "about_img": "https://lh3.googleusercontent.com/pw/AP1GczPBLs-aJWQ_4YjNDqDvo21Z7-u-okR61NIIR2S-M09U2QXvSPhAi8vDifje73RxKRkKvI_kQQE8_ZhYhiE8pQPoaTggnl1sMqI3SBtPiQJUz6P8qQ=w2400",
            "mission": "To equip believers through prayer, teaching God’s word, discipleship, evangelism, Christian living, tent-making so that they can be united, and attain the full knowledge of Christ in spiritual maturity",
            "vision": "To be a congregation of believers disciples under the five-fold ministry to fulfill the great commission of our Lord Jesus Christ.",
            "faith": "At Chrisco Central church, We offer a variety of services and programs to meet the spiritual needs of our congregation. Our Sunday services include uplifting music, inspiring sermons, and opportunities for personal growth and connection. We also have programs for children, youth, and adults throughout the week.",
            "faith_img": "https://lh3.googleusercontent.com/pw/AP1GczMYaAGwT0aYIN8hkaclRKO6CqakZ0edbSfB-tKiI45o2tzLWpgl3JxpT8SruXJq7OnNvV5KOS_x0EiuXENjjHjx1uOot3C_OoWHIpZqmoXitgWj0g=w2400",
            "word": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "word_img": "https://lh3.googleusercontent.com/pw/AP1GczNpNxFbo6ZXu_1n6niiIkAY_zKMR0Ewx9kyb6VuAVdxlHSN5tmkCENkbMyd69ud9JhSOvM1dIX-ik7Mh2vIe8WrRy4ZiyzJ4HEsv4znn-2OBzrYtA=w2400",
            "trinity": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "trinity_img": "https://lh3.googleusercontent.com/pw/AP1GczNoZV5rry2nzylb0Qxdbf72RJUzL706BOZKbiBM1I5bbfOcqrgVOqZGBLYlMpRqeGDHxmYnXONtgCN0D0xKQwBxZ2j3AOpKRzrpxkp_AjlJyw9mCw=w2400",
            "baptism": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris congue, dignissim nulla et, tincidunt velit. Sed libero arcu, convallis in eros vel, egestas congue nulla. Sed nec dictum nulla. Nulla facilisi. Aliquam erat volutpat. Sed non quam arcu. Donec euismod mauris.",
            "baptism_img": "https://lh3.googleusercontent.com/pw/AP1GczNTKQ0gT7R0jVOGrn1n6ngdiJx6n2CNfOIZ2xSNxRWaZF9kxozpUjmEinYv-y2QTiVB139nroDf06eO8jVF_ERNG2lqDvWLcD1odkYasIqckl2v6A=w2400",
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
        {
            "id": 1, 
            "title": "Teach to remember our days", 
            "content": "In the hustle and bustle of our daily lives, it's easy to get caught up in the whirlwind of activities, deadlines, and responsibilities. Yet, amidst the chaos, there lies a sacred journey unfolding—one that is filled with moments of grace, connection, and divine presence. As members of the church community, we are called to pause and reflect on the significance of time, recognizing it as a precious gift from the Creator. Each day is an opportunity to deepen our relationship with God, to serve others with love and compassion, and to bear witness to the beauty of creation.But how do we ensure that we make the most of our days, honoring them as sacred and meaningful? The answer lies in the ancient wisdom passed down through generations, teaching us to remember and cherish the moments that shape our lives. First and foremost, we are reminded to anchor our days in prayer and contemplation, setting aside time for quiet reflection and communion with the divine. Through prayer, we invite God into our midst, seeking guidance, strength, and peace for the journey ahead. Secondly, we are called to live with intentionality, embracing each moment with mindfulness and purpose. Whether it's sharing a meal with loved ones, lending a helping hand to those in need, or simply pausing to admire the beauty of nature, every act becomes an opportunity to experience God's presence in our midst. Moreover, we are encouraged to cultivate gratitude in our hearts, recognizing the blessings that surround us each day. From the warmth of the sun on our faces to the laughter of children playing in the church courtyard, there is much to be thankful for if only we open our eyes and hearts to see. Finally, we are invited to embrace the rhythm of the liturgical calendar, marking the seasons of the church year with reverence and joy. From Advent's hopeful anticipation to Easter's triumphant celebration, each season invites us to immerse ourselves fully in the story of salvation, experiencing anew the timeless truths of our faith. As we journey together through the sacred tapestry of time, let us heed the ancient wisdom that teaches us to remember our days, to cherish the moments that shape our lives, and to live each day with purpose, gratitude, and love.", 
            "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczNR_cU-twN3cJ0N2bhEST6ae5DNb_-fRw14dM8smmoLPpEX3kMlUzkO27HqUEpIkKCCGnXp88nPID3VjSgAkuwB92qobGL1-pCERWYUTo5fAr8MNg=w2400",
            "estimated_read_time": 3,
            "category_id": 2,
        },
        {
            "id": 2, 
            "title": "The Spirit of God gives us power to do new things", 
            "content": "In a world teeming with challenges and opportunities, it's easy to feel overwhelmed, unsure of our abilities to navigate the complexities of life. Yet, within each of us resides a boundless potential waiting to be unleashed. This potential finds its source in the timeless wisdom of the ages and the ever-present force that transcends human understanding—the Spirit of God. At the heart of many faith traditions lies the belief in a divine presence, a guiding force that animates creation and empowers individuals to transcend their limitations. For Christians, this presence is known as the Holy Spirit—a dynamic, life-giving energy that infuses believers with courage, wisdom, and creativity. The Scriptures attest to the transformative power of the Spirit, recounting stories of ordinary men and women who, upon receiving this divine gift, were emboldened to undertake extraordinary feats. From the prophets of old who spoke truth to power, to the disciples of Jesus who carried his message to the ends of the earth, the Spirit has always been the catalyst for change and renewal. In our own lives, too, the Spirit continues to work wonders, breathing new life into stagnant situations and inspiring us to dream dreams and envision possibilities beyond our wildest imaginations. It is the Spirit that whispers words of encouragement in moments of doubt, nudging us to step out in faith and embrace the unknown. But the Spirit's influence extends far beyond the realm of personal transformation. It empowers communities to come together in solidarity, to work towards a common vision of justice and peace. It emboldens advocates to speak out against oppression and injustice, to champion the cause of the marginalized and downtrodden. Indeed, the Spirit of God is the ultimate agent of change, the driving force behind all that is good and noble in the world. It is the source of our creativity, our resilience, our capacity to love and to forgive. With the Spirit as our guide, there is no limit to what we can achieve, no obstacle too great to overcome. So let us embrace the Spirit's presence in our lives, opening our hearts and minds to its transformative power. Let us draw strength from its wellspring of hope and inspiration, knowing that with God, all things are possible. And let us go forth with confidence, knowing that we are empowered by the Spirit to do new things, to bring about a brighter, more just and compassionate world for all.", 
            "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczPlvnommVZf1P-3nHAlgbCCLF1X9b4_n8K8m33dVOjNWNZ4ZDxFFAumZDftezsYHG71olCwpAxl8FkXN0EISFQU-WJbO6ppyBaYkDp6uvJrRn92IQ=w2400",
            "estimated_read_time": 3,
            "category_id": 1,
        },
        {
            "id": 3, 
            "title": "What shall I render unto to the Lord for all His benefits towards me", 
            "content": "In the tapestry of life, gratitude weaves threads of meaning, connecting us to something greater than ourselves. Among the profound questions posed by humanity, one echoes through the ages: 'What shall I render unto the Lord for all His benefits towards me?' As we traverse the landscape of existence, we encounter countless blessings, each a testament to the generosity of life itself. From the breath that fills our lungs to the sun's warmth on our skin, the universe bestows upon us its boundless gifts. Yet, in the face of such abundance, how do we reciprocate? How do we express our gratitude to the divine? Firstly, we may offer the gift of acknowledgment. In recognizing the blessings bestowed upon us, we honor the intricate web of interconnectedness that sustains our being. Every sunrise, every act of kindness, every moment of joy becomes a sacred offering, a testament to the profound beauty of existence. Secondly, we can cultivate the soil of our hearts with acts of kindness and compassion. By extending a hand to those in need, we embody the divine love that flows through us. Whether through charitable deeds, heartfelt words, or a simple smile, we sow the seeds of goodness, nurturing a world brimming with grace and abundance. Moreover, gratitude beckons us to embrace the present moment with reverence and awe. In the midst of life's challenges and triumphs, we find solace in the eternal now, where every breath is a divine communion, every heartbeat a sacred rhythm. By living mindfully, we infuse each moment with purpose and meaning, enriching our lives with the vibrant tapestry of experience. Yet, perhaps the greatest offering we can give is the gift of ourselves. In surrendering to the divine will, we become vessels of love and light, conduits for the infinite grace that flows through us. Through prayer, meditation, and acts of devotion, we open our hearts to the divine presence, allowing it to guide us on our journey homeward. In conclusion, the question 'What shall I render unto the Lord for all His benefits towards me?' transcends mere words and deeds; it calls upon us to embody the very essence of gratitude itself. Through acknowledgment, kindness, presence, and surrender, we become living expressions of divine love, illuminating the world with the radiance of our souls. So let us offer our hearts as temples of gratitude, for in doing so, we become one with the eternal dance of life itself.", 
            "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczOtyAi7X2-R5y1U4XlT_BQJhg5fAVwqBGkp-I5S0H_VEt5JsgW5K0vtcBfOZ3-2lONw1mplBCwJJdy6JHMyr4Qa3feuG1vicRofjJ-eaEoNcD3X5g=w2400",
            "estimated_read_time": 2,
            "category_id": 2,
        },
        {
            "id": 4, 
            "title": "Paul pursuit of the prize: Pressing towards the goal", 
            "content": "In the annals of history, few figures stand as tall as the Apostle Paul, whose unwavering commitment to his mission and unyielding perseverance serve as an inspiration for generations. Amidst the challenges of his time, Paul's pursuit of the prize, as articulated in his letters and actions, encapsulates a profound journey of faith, determination, and purpose. Paul's pursuit was not merely for earthly accolades or fleeting rewards but for an eternal prize, a crown that transcends the confines of mortal existence. His words echo through the corridors of time, urging believers to press towards the goal with the same fervor and dedication that marked his own life. At the heart of Paul's pursuit was a singular focus: the advancement of the Gospel. From his dramatic conversion on the road to Damascus to his tireless missionary journeys, Paul's life was a testament to the transformative power of faith and the relentless pursuit of truth. In his letter to the Philippians, Paul writes, 'I press on toward the goal for the prize of the upward call of God in Christ Jesus' (Philippians 3:14, ESV). These words encapsulate the essence of his journey – an unwavering commitment to follow Christ, regardless of the obstacles or trials that lay ahead. Paul's pursuit was marked by sacrifice and suffering, yet he remained steadfast in his resolve. He endured imprisonment, shipwrecks, and persecution, yet his faith never wavered. It was this steadfastness that set him apart, inspiring countless believers to stand firm in the face of adversity. But Paul's pursuit was not a solitary endeavor. He understood the importance of community and collaboration in advancing the Kingdom of God. His letters to the early churches served as a rallying cry for believers to unite in purpose and mission, laying aside their differences for the sake of the Gospel. As we reflect on Paul's pursuit of the prize, we are reminded of the enduring legacy of faith and perseverance. In a world marked by uncertainty and turmoil, his example shines as a beacon of hope, urging us to fix our eyes on Jesus and press towards the goal with unwavering resolve. May we, like Paul, embrace the call to pursue the prize with all our hearts, knowing that our labor in the Lord is not in vain. And may we, too, one day hear the words, 'Well done, good and faithful servant. Enter into the joy of your Master' (Matthew 25:21, ESV), as we receive the ultimate prize – eternal life in Christ Jesus.", 
            "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczPGKg59zsgPLDv12_riXKlfPflGAz4-YU8G6YJCDIRq3u57WA8BF9-WrkKijSk6FcSZkYBgcAWEsfrq1l2rQSCOurmTSQt6P5QeLx6O80KLCa7CEQ=w2400",
            "estimated_read_time": 3,
            "category_id": 3,
        },
        {
            "id": 5, 
            "title": "When the winds howl and the waves crash around us", 
            "content": "In the tumultuous journey of faith, there are moments when the winds howl and the waves crash around us, threatening to engulf us in doubt and fear. Yet, it is precisely in these tempests that the essence of Christianity reveals itself. The imagery of winds and waves holds profound significance within the Christian narrative. It evokes the scene of Jesus calming the stormy sea, demonstrating his power over nature and his ability to bring peace amidst chaos. This story serves as a timeless reminder that even in the fiercest storms of life, there is hope to be found in the unwavering presence of God. When the winds of adversity blow relentlessly, and the waves of uncertainty loom large, it's natural to feel overwhelmed and disheartened. We may question the very foundations of our faith, wondering why a loving God would allow such trials to beset us. Yet, it is precisely in these moments that our faith is tested and refined. For it is not in the absence of storms that faith finds its strength, but rather in the midst of them. It is in the moments of doubt and despair that we are called to anchor our trust in God's promises, knowing that He is with us always, guiding us through the darkest of nights. The Apostle Paul, no stranger to trials and tribulations, wrote, 'We are afflicted in every way, but not crushed; perplexed, but not driven to despair; persecuted, but not forsaken; struck down, but not destroyed' (2 Corinthians 4:8-9). These words resonate deeply with the essence of Christian faith — a faith that endures in the face of adversity, a faith that finds strength in weakness, and a faith that perseveres against all odds. In the grand tapestry of Christian history, we find countless examples of individuals who weathered the storms of life with unwavering faith and courage. From the martyrs who faced persecution with steadfast resolve to the saints who found solace in the midst of suffering, their stories serve as beacons of hope for all who journey through the trials of faith. Ultimately, the winds may howl, and the waves may crash, but the foundation of our faith remains unshaken. For in Christ, we find the anchor of our souls, the rock upon which we stand firm amidst the storms of life. And as we navigate the turbulent waters of faith, may we find comfort in the words of Jesus: 'Take heart; it is I. Do not be afraid' (Matthew 14:27).", 
            "blog_img": "https://lh3.googleusercontent.com/pw/AP1GczNhzcahl8n5w8gHaNoxYB0Lq-Mqsnf_KRBIhvd3_xNa6OtZQNuKIqCRZyoMEqsyMo3C31qq9Gwk4mGO3-0tB0reyBCYnwwyIsWpFF4Zxy5gOO-H0Q=w2400",
            "estimated_read_time": 1,
            "category_id": 3,
        },
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

    categories_data = [
        {"id": 1, "name": "Sermons", "slug": "sermons"},
        {"id": 2, "name": "Outreach", "slug": "outreach"},
        {"id": 3, "name": "Theological Insights", "slug": "theology"},
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