# entering data into db using pymysql
import pymysql
import datetime

# creating a connection
connection = pymysql.connect(user='root', password='password1996', host='localhost', database='orm')

# creating a cursor
cursor = connection.cursor()

# local data structure
data = {
        "heading":"Sisterly Love: A Journey of Endless Support and Unconditional Bond",
        "subheading": "A Heartfelt Tribute to the Sister Who Filled My Life with Warmth and Affection",
        "author": "David Harrison",

        "content": 

        '''In the symphony of family, my sister's presence is a melody that resonates with love and unwavering support. From the earliest days of childhood to the complexities of adulthood, she has been my confidante, my companion, and my biggest cheerleader, making each step of life's journey more meaningful and joyful.

Our sisterly bond is a treasure that only grows with time. From playful moments to heart-to-heart conversations, we have shared experiences that have enriched our lives. Her presence brings a sense of comfort, knowing that I have someone by my side who understands me in ways that no one else can.

In moments of joy, she celebrates my triumphs as if they were her own. Her genuine happiness for my successes lifts my spirits and fills my heart with gratitude. In times of sorrow, she lends a listening ear, providing comfort and reassurance that I am not alone in facing life's challenges.

Our bond is strengthened by shared memories and a history that only siblings can share. We have grown together, learning from each other's strengths and weaknesses. In her, I see a reflection of myself and the values instilled in us by our parents. She has taught me the importance of resilience, kindness, and the power of a supportive heart.

As we grew older, our bond transcended the confines of blood relations and blossomed into an enduring friendship. We have become each other's pillars of strength, offering unwavering support in times of need and celebrating the small victories that make life worthwhile.

Through the twists and turns of life, my sister's unwavering love has been a constant beacon of light. Her compassion knows no bounds, and her empathy is a balm for the soul. I am humbled by her selflessness and the depth of her care.

This tribute is a celebration of my sister, a person who holds a special place in my heart. She is not just a sibling but also a friend, a mentor, and a source of endless inspiration. Her love has shaped me into a better person, and I am forever grateful for the gift of calling her my sister.

As we continue to navigate life's journey, I know that our bond will remain steadfast. Through the highs and lows, the laughter and tears, we will stand side by side, supporting each other, and cherishing the precious moments we share as sisters and friends.''',

        "date": datetime.datetime.utcnow(),
        "image": "home-bg.jpg",
        "slug": 'my-sister'
        }

# insert query
insert_query = "INSERT INTO blogpost (heading, subheading, author, date, image, content, slug) VALUES (%s, %s, %s, %s, %s, %s, %s)"

# values 
values = (data['heading'], data['subheading'], data['author'], data['date'], data['image'], data['content'], data['slug'])

# executing the query
cursor.execute(insert_query, values)

# committing it
connection.commit()

# closing the cursor and connections
cursor.close()
connection.close()