import random

# Quiz is a class that contains all the information on a movieguessinggame
# this class is necessary in order to differentiate the different games for the different users.


class Quiz:
    def __init__(self) -> None:

        # possible Quizzes
        self.questions = [
            ("π³ββοΈ π£ π―", "life of pi"),
            ("π§ πΈ π", "princess and the frog"),
            ("π β¨ π© π", "gravity"),
            ("5οΈβ£ 0οΈβ£ 0οΈβ£ π β€οΈ", "500 days of summer"),
            ("πͺ π© πΏ", "psycho"),
            ("π§ β β βοΈ", "Airplane"),
            ("π¨ π¨ β€οΈ ποΈ", "Brokeback mountain"),
            ("π―π΅ π£ πΊπΈ β", "pearl harbour"),
            ("π  π°ββοΈ β π", "cinderella"),
            ("π¦ π  π¨ π¨", "home alone"),
            ("πΌ βͺ πΉ", "angels and demons"),
            ("π π² π π π", "ratatouille"),
            ("βοΈ π π", "the notebook"),
            ("π³ β‘οΈ π", "free willy"),
            ("π©οΈ π¨ π¨", "thor"),
            ("π©Έ π", "Blood diamond"),
            ("π₯ π£ π»", "Scary Movie"),
            ("π¨ β‘οΈ π", "Santa Clause"),
            ("π π π π", "Planet of the apes"),
            ("πΌ π", "Kung Fu Panda"),
            ("π¨ π§Έ π»", "Ted"),
            ("π¦ π« π­", "Charlie and the chocolate factory"),
            ("π π π ", "The devil wears prada"),
            ("π’ π§ ποΈ", "Titanic"),
            ("π¦ π β‘οΈ π", "Lord of the rings"),
            ("π½ π π π¦ π² π", "ET"),
            ("π΄ π β€οΈ", "Eat Pray Love"),
            ("πββοΈ π«π· πΈ πΆ", "Les misΓ©rables"),
            ("π π¬ π€", "The kings speech"),
            ("π π¦ π¨ π¦ πΏ π", "night at the museum"),
        ]

        # randomized choice of a quiz and optional choose options for Easy playmode
        self.round = random.randint(0, len(self.questions) - 1)
        self.false1 = random.randint(0, len(self.questions) - 1)
        self.false2 = random.randint(0, len(self.questions) - 1)
        self.false3 = random.randint(0, len(self.questions) - 1)

        # guesscount for hard mode
        self.guesscount = 0

        # setting the answer and the question of the Quiz with the previously randomly chosen self.quiz variable
        self.answer = self.questions[self.round][1]
        self.question = self.questions[self.round][0]

        # initializing the variable playmodus
        self.playmodus = None

        # setting the answer options for the Easy mode by using the previously randomly chosen self.false1, self.false2 and self.false3 variables
        self.option1 = self.questions[self.false1][1]
        self.option2 = self.questions[self.false2][1]
        self.option3 = self.questions[self.false3][1]
