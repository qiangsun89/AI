import gym
# 创建环境
env = gym.make('CartPole-v1',render_mode="rgb_array")

# 初始化环境
env.reset()

for _ in range(1000):
    env.render()  # 渲染环境以便于观察

    # 在这个示例中，我们只是随机选择动作
    action = env.action_space.sample() 

    # 执行动作，并获得环境的反馈信息
    observation, reward, done, truncated,info = env.step(action)

    if done:
        env.reset()  # 如果杆子倒下，重置环境

env.close()  # 关闭环境