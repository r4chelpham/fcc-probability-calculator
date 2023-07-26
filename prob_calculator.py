import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.balls = dict()
    self.contents = []
    if not kwargs:
      raise ValueError("At least one keyword argument is required.")
    self.balls = kwargs
    for ball in self.balls.keys():
      for b in range(self.balls[ball]):
        self.contents.append(ball)
        
  def draw(self, amount):
    if amount > len(self.contents):
      return self.contents
      
    colour_balls = []
    for i in range(amount):
      index = random.randint(0,len(self.contents)-1)
      colour = self.contents[index]
      self.balls[colour] -= 1
      colour_balls.append(colour)
      self.contents.remove(colour)

    return colour_balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count_balls = 0
  
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    ball_count = dict()
    for ball in drawn_balls:
      ball_count[ball] = ball_count.get(ball, 0) + 1

    same_outcome = 0

    for ball in expected_balls.keys():
      count = ball_count.get(ball, 0)
      
      if count == 0:
        continue
      if count >= expected_balls[ball]:
        same_outcome += 1
        
    if same_outcome == len(expected_balls):
      count_balls += 1
  
  return count_balls/num_experiments