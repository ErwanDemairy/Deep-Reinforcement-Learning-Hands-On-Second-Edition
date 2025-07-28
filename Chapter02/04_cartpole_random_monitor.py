import gymnasium as gym


if __name__ == "__main__":
    env = gym.make("CartPole-v0", render_mode="rgb_array")
    trigger = lambda t: t % 10 == 0
#    env = gym.wrappers.Monitor(env, "recording")
    env = gym.wrappers.RecordVideo(env, video_folder="./save_videos1", episode_trigger=trigger, disable_logger=True)
   # env = gym.wrappers.RecordVideo(env, "recording")

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, _, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))
    env.close()
    env.env.close()
