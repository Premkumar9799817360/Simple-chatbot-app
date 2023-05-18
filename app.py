import streamlit as st
import nltk
from nltk.chat.util import Chat 

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Teacher (because give the all answer), but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
     [
        r"I am fine",
        ["Great to hear that! How can I assist you today?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Prem Kumar created me using Python's NLTK library ","top secret ;)",]
    ],
     [
        r"(.*)father(.*)",
        ["Prem Kumar created me using Python's NLTK library",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pali, Jaipur',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
   
    #study
       [
        r"how can I improve my (.* )?study skills",
        ["To improve your study skills, you can try the following:\n1. Create a study schedule and stick to it.\n2. Break your study sessions into smaller chunks.\n3. Find a quiet and comfortable study environment.\n4. Take effective notes during lectures.\n5. Practice active learning techniques.\n6. Seek help from your instructors or peers when needed.",]
    ],
    [
        r"(.*) study tips",
        ["Here are some general study tips:\n1. Stay organized.\n2. Set specific goals.\n3. Use mnemonic devices to remember information.\n4. Take regular breaks during study sessions.\n5. Review and summarize your notes.\n6. Use online resources and educational platforms.\nRemember, everyone has different study preferences, so find what works best for you!",]
    ],
    [
        r"recommend (me|some) (books|resources) for (.*)",
        ["Sure! Here are some recommended %2 for %3:\n1. [Book/Resource 1]\n2. [Book/Resource 2]\n3. [Book/Resource 3]\nFeel free to explore these options and find the ones that align with your study goals.",]
    ],
    [
        r"What will life be like in the future\?",
        ["The future holds many possibilities. Life could be more automated, interconnected, and technologically advanced.",]
    ],
    [
        r"How will technology shape our future\?",
        ["Technology will likely play a significant role in shaping the future. It may lead to advancements in various fields like AI, robotics, healthcare, and transportation.",]
    ],
     [
        r"(.*) technology (.*)",
        ["Technology will likely play a significant role in shaping the future. It may lead to advancements in various fields like AI, robotics, healthcare, and transportation.",]
    ],
    [
        r"Will robots take over our jobs\?",
        ["While automation may replace certain jobs, it's also expected to create new opportunities. It's important for humans to adapt and acquire skills that complement emerging technologies.",]
    ],
    [
        r"What advancements can we expect in healthcare\?",
        ["In the future, healthcare could witness breakthroughs in personalized medicine, genomics, telemedicine, and AI-driven diagnostics, leading to improved treatments and better health outcomes.",]
    ],
    [
        r"How will transportation change in the future\?",
        ["Transportation could become more autonomous and sustainable. Electric vehicles, self-driving cars, hyperloop systems, and drones may revolutionize how we commute and transport goods.",]
    ],
    [
        r"What will future cities look like\?",
        ["Future cities may prioritize sustainability, smart infrastructure, and efficient resource management. They could integrate renewable energy, IoT devices, green spaces, and advanced urban planning.",]
    ],
    [
        r"What challenges will humans face in the future\?",
        ["The future may bring challenges such as ethical dilemmas around AI, privacy concerns, climate change, and socio-economic disparities. Addressing these issues will be crucial for a positive future.",]
    ],
    [
        r"Will humans colonize other planets\?",
        ["Space exploration and colonization are actively pursued by various organizations. In the future, humans may establish settlements on other planets or celestial bodies, expanding our presence beyond Earth.",]
    ],
    # health
    [
        r"(.*) tips for a healthy life",
        [
            "Here are some tips for a healthy life:\n1. Eat a balanced diet with plenty of fruits and vegetables.\n2. Stay hydrated by drinking an adequate amount of water.\n3. Engage in regular physical activity or exercise.\n4. Get enough sleep to rest and rejuvenate.\n5. Manage stress through relaxation techniques like meditation or deep breathing.\n6. Avoid smoking and limit alcohol consumption.\n7. Maintain a healthy weight through portion control and regular exercise.\n8. Practice good hygiene, including regular handwashing.\n9. Stay socially connected with friends and family.\n10. Schedule regular check-ups and screenings with your healthcare provider."
        ]
    ],
    [
        r"(.*) eat healthy(.*)",
        [
            "Eating healthy is crucial for maintaining a healthy life. Here are some tips:\n1. Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your diet.\n2. Limit processed and sugary foods and drinks.\n3. Control portion sizes to avoid overeating.\n4. Cook meals at home using fresh ingredients.\n5. Read food labels to make informed choices.\n6. Stay mindful of your eating habits and listen to your body's hunger and fullness cues.\n7. Stay hydrated by drinking water throughout the day.\n8. Avoid skipping meals and try to eat regular, balanced meals.\n9. Seek guidance from a registered dietitian for personalized advice."
        ]
    ],
    [
        r"(.*) exercise(.*)",
        [
            "Regular exercise is important for a healthy life. Here are some exercise tips:\n1. Aim for at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous-intensity aerobic activity every week.\n2. Include strength training exercises at least twice a week.\n3. Find activities you enjoy, such as walking, jogging, cycling, swimming, or dancing.\n4. Start with small steps and gradually increase the intensity and duration of your workouts.\n5. Stay consistent with your exercise routine.\n6. Warm up before exercising and cool down afterward.\n7. Listen to your body and modify exercises as needed.\n8. Consult with a healthcare professional before starting a new exercise program."
        ]
    ],
    [
        r"(.*) get enough sleep(.*)",
        [
            "Getting enough sleep is essential for your overall well-being. Here are some tips:\n1. Aim for 7-9 hours of quality sleep each night.\n2. Establish a regular sleep schedule by going to bed and waking up at consistent times.\n3. Create a sleep-friendly environment that is cool, dark, and quiet.\n4. Avoid electronic devices, caffeine, and heavy meals close to bedtime.\n5. Establish a relaxing bedtime routine to signal your body that it's time to sleep.\n6. Manage stress and anxiety through relaxation techniques.\n7. If you have trouble sleeping, consider speaking to a healthcare professional."
        ]
    ],
    [
        r"(.*) manage stress(.*)",
        [
            "Managing stress is important for your mental and physical health. Here are some tips:\n1. Practice relaxation techniques like deep breathing, meditation, or yoga.\n2. Engage in regular physical activity, which can help reduce stress levels.\n3. Prioritize self-care activities that bring you joy and relaxation.\n4. Maintain a healthy work-life balance.\n5. Seek support from friends, family, or a therapist.\n6. Practice time management and set realistic goals.\n7. Avoid excessive alcohol or drug use as coping mechanisms.\n8. Find healthy ways to cope with stress, such as journaling or engaging in hobbies."
        ]
    ],
    [
        r"(.*) motivation(.*)",
        [
            "Motivation is what drives you to take action and achieve your goals. What specifically do you need motivation for \n1 Motivation is the key to success! What do you need motivation for? \n2 Motivation is like fuel for your dreams. How can I help you find motivation?",
        ]
    ],
    [
        r"(.*) unmotivated (.*)",
        [
            "Feeling unmotivated happens to everyone from time to time. What do you think might be causing it? \n1 It's normal to have periods of feeling unmotivated. What usually helps you get back on track? \n2 When you're feeling unmotivated, try breaking your tasks into smaller, manageable steps. What's been on your mind lately?",
        ]
    ],
    [
        r"(.*) overcome procrastination(.*)",
        [
            "To overcome procrastination, try breaking your tasks into smaller, actionable steps. Start with something small and build momentum. What task are you currently procrastinating on? \n2 Procrastination can be tough, but taking the first step is often the hardest part. What usually helps you get started? \n1 One way to overcome procrastination is by setting specific goals and deadlines. Have you tried using a planner or setting reminders?",
        ]
    ],
    [
        r"(.*) achieve goals",
        [
            "To achieve your goals, start by setting clear and specific objectives. Break them down into smaller milestones and track your progress. What goals are you currently working towards. Consistency and perseverance are key to achieving your goals. What steps have you taken so far. Visualize your goals and create a plan of action. Stay focused and remind yourself of the reasons why you want to achieve them. What's your biggest goal right now?",
        ]
    ],
    [
        r"(.*) feeling demotivated(.*)",
        [
            "When feeling demotivated, take a step back and reflect on your reasons for pursuing your goals. Surround yourself with positive influences and seek support from others. What has been bringing you down lately.Sometimes a change in routine or environment can help rekindle motivation. Have you considered trying something new or exploring different approaches. Remember that setbacks are part of the journey. Embrace them as learning experiences and keep pushing forward. Is there something specific that's been affecting your motivation?",
        ]
    ],
    [
        r"(.*) success(.*)",
        [
            "Success means different things to different people. How do you define success for yourself. Success is the result of hard work, determination, and perseverance. What are some of your personal definitions of success. Success is not just about achieving goals but also about personal growth and fulfillment. How do you measure your own success?",
        ]
    ],
    [
        r"(.*) dream(.*)",
        [
            "Dreams are powerful motivators. What is your dream, and what steps are you taking to make it a reality? Dreams give us something to strive for. How do you plan on turning your dreams into actionable goals? Remember that dreams can be achieved with dedication and perseverance. What steps have you already taken towards your dream?",
        ]
    ],
    [
        r"(.*) believe in yourself(.*)",
        [
            "Believing in yourself is essential. Remember your past achievements and strengths. You are capable of great things! What has been challenging your self-belief lately? \n1 Self-belief is a powerful tool. Surround yourself with positive affirmations and supportive people. How can I help boost your self-belief?\n2 Believe in your abilities and keep pushing forward. You've got this! Is there a specific area where you're struggling to believe in yourself?",
        ]
    ],
    [
        r"(.*) stay motivated(.*)",
        [
            "Staying motivated requires finding what inspires you. Set meaningful goals, celebrate milestones, and find joy in the process. What usually helps you stay motivated? \n1 Motivation can fluctuate, but you can cultivate it by practicing self-care, maintaining a positive mindset, and focusing on your purpose. What activities or strategies have worked for you in the past? \n2 Remember your 'why' and surround yourself with positive influences. What's been challenging your motivation recently?",
        ]
    ],
    #maths
    [
        r"What is the formula for the area of a circle?",
        ["The formula for the area of a circle is A = π * r^2, where A is the area and r is the radius.",]
    ],
     [
        r"area of circle?",
        ["The formula for the area of a circle is A = π * r^2, where A is the area and r is the radius.",]
    ],
    [
        r"What is the speed of light?",
        ["The speed of light in a vacuum is approximately 299,792,458 meters per second.",]
    ],
    [
        r"What is Newton's second law of motion?",
        ["Newton's second law of motion states that the force acting on an object is equal to the mass of the object multiplied by its acceleration.",]
    ],
    [
        r"What is the value of π?",
        ["The value of π (pi) is approximately 3.14159.",]
    ],
      [
        r"(.*)value of pi?",
        ["The value of π (pi) is approximately 3.14159.",]
    ],
    [
        r"What is the equation for the Pythagorean theorem?",
        ["The equation for the Pythagorean theorem is a^2 + b^2 = c^2, where a and b are the lengths of the two shorter sides of a right triangle, and c is the length of the hypotenuse.",]
    ],
    [
        r"What is the atomic number of carbon?",
        ["The atomic number of carbon is 6.",]
    ],
    [
        r"What is the chemical formula for water?",
        ["The chemical formula for water is H2O.",]
    ],
       [
        r"what is python\?",
        ["Python is a high-level programming language known for its simplicity and readability.",]
    ],
    [
        r"what are the features of python\?",
        ["Python has several features including dynamic typing, automatic memory management, and a large standard library.",]
    ],
    [
        r"what is a variable in programming\?",
        ["A variable is a named storage location used to store data in a program.",]
    ],
    [
        r"what is a loop in programming\?",
        ["A loop is a programming construct that allows the repeated execution of a block of code.",]
    ],
     [
        r"what should I wear for an interview\?",
        ["It's best to dress professionally for an interview. Consider wearing formal attire such as a suit or a business outfit.",]
    ],
    [
        r"how should I prepare for an interview\?",
        ["To prepare for an interview, research the company, practice common interview questions, and be ready to discuss your qualifications and experiences.",]
    ],
    [
        r"what are common interview questions\?",
        ["Common interview questions include 'Tell me about yourself', 'Why do you want to work for this company?', 'What are your strengths and weaknesses?', etc.",]
    ],
    [
        r"how do I answer the 'Tell me about yourself' question\?",
        ["When answering 'Tell me about yourself', briefly introduce yourself, mention your educational background, highlight relevant experiences, and emphasize your skills.",]
    ],
    [
        r"what questions should I ask the interviewer\?",
        ["You can ask about the company culture, opportunities for growth, the team you'll be working with, or any specific questions about the role or responsibilities.",]
    ],
    [
        r"what is machine learning ?",
        ["Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and models that enable computers to learn and make predictions or decisions without being explicitly programmed.",]
    ],
     [
        r"(.*) machine learning ?",
        ["Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and models that enable computers to learn and make predictions or decisions without being explicitly programmed.",]
    ],
    [
        r"what are the types of machine learning?",
        ["There are three main types of machine learning: supervised learning, unsupervised learning, and reinforcement learning.",]
    ],
    [
        r"what is supervised learning?",
        ["Supervised learning is a type of machine learning where the model is trained on labeled examples, with input-output pairs. It learns to predict the output given the input.",]
    ],
    [
        r"what is unsupervised learning?",
        ["Unsupervised learning is a type of machine learning where the model is trained on unlabeled data. It discovers patterns and relationships in the data without any predefined labels.",]
    ],
    [
        r"what is reinforcement learning?",
        ["Reinforcement learning is a type of machine learning where an agent learns to interact with an environment and takes actions to maximize rewards. It learns through trial and error.",]
    ],
    [
        r"what are some popular machine learning algorithms?",
        ["Some popular machine learning algorithms include linear regression, logistic regression, decision trees, random forests, support vector machines, and neural networks.",]
    ],
  
    [
        r"what is deep learning?",
        ["Deep learning is a subfield of machine learning that focuses on neural networks with multiple layers. These deep neural networks can learn hierarchical representations of data, enabling them to capture complex patterns and relationships.",]
    ],
    [
        r"what are some applications of machine learning?",
        ["Machine learning has various applications, such as image and speech recognition, natural language processing, recommendation systems, autonomous vehicles, and fraud detection, to name a few.",]
    ],
     [
        r"(.*)",
        ['Sorry answer is not available in data']
    ],
]
chat = Chat(pairs)
def main():
    st.title("Simple Chatbot App 💾")
    st.header("Eample of Ask question")
    st.text("1.father or city or location or I am fine or help or sorry or hello")
    st.text("2.believe in yourself or dream or feeling demotivated or success")
    st.text("3.What is study tips or technology")
    st.text("4.what are common interview questions")
    st.text("5.What are the features of Python")
    st.text("6.what is machine learning")
    st.text("7.what is exercise for me or what is eat healthy")
    st.header("🙎‍♂️")
    user_input = st.text_input("User🙎‍♂️:")

    if st.button("Send 🔎"):
        response = chat.respond(user_input)
        st.header("🤖")
        st.text_area("Chatbot🤖:",value=response)

if __name__ == '__main__':
    main()
st.header("Created by Prem Kumar") 
