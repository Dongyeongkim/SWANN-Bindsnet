import time
import torch
from bindsnet.encoding import bernoulli
from bindsnet.environment import GymEnvironment
from bindsnet.pipeline import EnvironmentPipeline
from bindsnet.pipeline.action import select_softmax



def return_score(network_list):

    def run_pipeline(pipeline, episode_count):
        for i in range(episode_count):
            total_reward = 0
            pipeline.reset_state_variables()
            is_done = False
            while not is_done:
                result = pipeline.env_step()
                pipeline.step(result)

                reward = result[1]
                total_reward += reward

                is_done = result[2]
        print(f"Episode {i} total reward:{total_reward}")
        return total_reward

    score_sum = 0; score_list = []
    for network in network_list:
        if torch.cuda.is_available():
            network.cuda()
        else:
            pass
        environment = GymEnvironment("BreakoutDeterministic-v4")
        environment.reset()
        # Build pipeline from specified components.
        environment_pipeline = EnvironmentPipeline(
            network,
            environment,
            encoding=bernoulli,
            action_function=select_softmax,
            output="Output Layer",
            time=100,
            history_length=1,
            delta=1,
            plot_interval=1,
            render_interval=1,
        )
        print("Training: ")
        run_pipeline(environment_pipeline, episode_count=10)

        # stop learning
        environment_pipeline.network.learning = False

        print("Testing: ")
        score_sum += run_pipeline(environment_pipeline, episode_count=10)
        score_list.append(score_sum/10)
        time.sleep(2)
        torch.cuda.empty_cache()
        

    return score_list



