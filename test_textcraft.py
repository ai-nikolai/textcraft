from textcraft import TextCraft

def main():
    env = TextCraft()
    obs, info = env.reset(seed=42)
    print(obs)
    action = input("> ")
    while action:
        (observation, reward, terminated, truncated, info) = env.step(action)
        print(observation, reward, sep="\n")
        action = input("> ")

if __name__=="__main__":
    main()