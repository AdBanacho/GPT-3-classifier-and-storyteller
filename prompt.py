def generate_prompt_greetings(name):
    return """Say words of welcome.

    Member: Pawel
    Greetings: Hi Paweł! Welcome to our Adrian's portfolio! We're glad to have you here.
    Member: New Native
    Greetings: Welcome, New Native! We are excited to have you as visitor of our portfolio.
    Member: Igor
    Greetings: Hello, Igor! It's a pleasure to have you here. Look on this portfolio.
    Member: {}
    Greetings:""".format(name.capitalize())


def generate_prompt_story(topic):
    return """Create a story.
    Topic: Adrian's job interview
Two-Sentence Story: Adrian arrived early for his job interview, but the receptionist told him he would have to wait a few minute. Adrian tried to stay calm, but he was getting more and more nervous as the minutes ticked by. Finally, the interviewer came out and Adrian tried his best to impress.

Topic: Adrian's job interview
Two-Sentence Story: Adrian arrived at the office building for his job interview 15 minutes early. He nervously checked his appearance in the lobby mirror and straightened his tie. When the elevator doors opened, he stepped inside and pushed the button for the top floor.

Topic: Adrian's job interview
Two-Sentence Story: Adrian was nervous for his job interview, but he tried to remain calm. He answered all of the questions truthfully and to the best of his abilities. In the end, he was offered the job and he was very happy.

Topic: Adrian's job interview
Two-Sentence {} Story:""".format(topic)


def generate_prompt_main_words(sentence):
    return """Find nouns.
sentence: Adrian was very nervous for his job interview, but he tried to remain calm. When the interviewer asked him a question, he accidentally blurted out the answer in a very high-pitched voice. The interviewer looked surprised, but Adrian was offered the job anyway.
words: question, answer, voice, interviewer

sentence: Adrian was waiting for his job interview when he heard a voice from the other room. It sounded like the interviewer was talking to someone, but Adrian couldn't make out what they were saying. Suddenly, the door opened and the interviewer motioned for Adrian to come in. As Adrian entered the room, he saw the interviewer talking to a skeleton.
words: sound, room, interviewer, skeleton

sentence: Adrian was very nervous for his job interview, and he accidentally farted when he sat down. He was so embarrassed, but he tried to act like nothing happened. The interviewer didn't seem to notice, and Adrian was eventually offered the job.
words: fart, embarrassment, interviewer, job.

sentence: Adrian was waiting for his job interview when he heard a scream from the office. He got up to investigate and saw the interviewer with his throat slit. Adrian ran away and called the police.
words:  scream, office, throat, police

sentence: {}
words: """.format(sentence)


def generate_prompt_music(none):
    return """Write words for a song."""




