from scheduler import Scheduler
env = Scheduler(n=5, mt=2, mr=6)
some_random_action = env.sample() #sample() returns a randomly sampled action
print(some_random_action)
state, reward, done, observation = env.step(some_random_action)
print(f"Reward is: {reward}")
print(f"Obsevation is: {observation}")
if done:
  print(f"Episode done, call reset().")
env.render(True)
env.render(False)
