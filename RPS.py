# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play,my_history = []):
    winning_set = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }
    if len(my_history)>1:
      if (winning_set[my_history[-1]]==prev_play):
        guess = winning_set[prev_play]
      else:
        guess = winning_set[my_history[-1]]
    else:
      guess = "P"
    my_history.append(guess)
    return guess