import random as r

class Quiz:
  def __init__(self, name="Player 1"):
    self.questions = {
      "What is the capital of Nevada?": "Carson City",
      "What is the world record for most soap bubble bounces using bubble wand?": "113",
      "What is the most well-known Pokémon character?": "Pikachu",
      "How many books are there in the Percy Jackson and the Olympians series?": "6",
      "Which is bigger, America or Africa?": "Africa",
      "What computer language was used to program windows?": "C++",
      "In what year was the first video game made?": "1958",
      "What is the largest ocean on earth?": "The Pacific Ocean",
      "When was the first electronic digital computer built?": "1939",
      "When was Facebook launched?": "2004",
      "How many dwarf planets are there in our solar system?": "5",
      "When did the first person to walk on the moon?": "1969",
      "What is the largest animal on the planet?": "Blue Whale",
      "What year was Leonardo da Vinci born?": "1452",
      "When was the character of Mickey Mouse created?": "1928",
      "When was the first chocolate bar invented?": "1847",
      "What is the atomic symbol for gold?": "Au",
      "When was the first Apple iPhone created?": "2007",
      "When was the international space station launched into space?": "1994",

    }
    self.player = name
  
  def handlePick(self):
    picker = list(self.questions.keys())
    rand = r.randint(0, len(picker))
    return picker[rand]

  def startGame(self):
    seen = {""}
    print("Welcome to Trivia Master Version 468674.62,", self.player, "👾")
    
    correct = 0
    for i in range(10):
      question = self.handlePick()
      while question in seen:
        question = self.handlePick()
      print(question)
      answer = self.questions.get(question)
      seen.add(question)
      guess = input()
      counter = 3
      if guess == self.questions.get(question):
        print("Correct😃!!!")
        correct += 1
      while guess != answer:
        counter -= 1
        print("Incorrect😢...")
        print(str(counter), "tries left ")
        guess = input()
        if guess == self.questions.get(question):
          print("Correct😃!!!")
          correct += 1
        if counter == 1 and guess != self.questions.get(question):
          if i < 5:
            print("Out of tries")
          break



      if i < 5:
        print("Next question")
      else:
        print("Game over.")
        if correct >= 3:
          print("You won😃🥳🤩🎉!!!")
        else:
          print("You lost😭...")

game = Quiz("Derek")
game.startGame()