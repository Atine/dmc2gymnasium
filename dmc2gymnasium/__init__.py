import gymnasium
from gymnasium.envs.registration import register


def make(
    domain_name,
    task_name,
    seed=1,
    visualise_reward=True,
    from_pixels=False,
    height=84,
    width=84,
    camera_id=0,
    frame_skip=1,
    episode_length=1000,
    environment_kwargs=None,
    time_limit=None,
    channels_first=True,
):
    env_id = "dmc_%s_%s_%s-v1" % (domain_name, task_name, seed)

    if from_pixels:
        assert (
            not visualise_reward
        ), "cannot use visualise reward when learning from pixels"

    # shorten episode length
    max_episode_steps = (episode_length + frame_skip - 1) // frame_skip

    if env_id not in gymnasium.envs.registry:
        task_kwargs = {}
        if seed is not None:
            task_kwargs["random"] = seed
        if time_limit is not None:
            task_kwargs["time_limit"] = time_limit
        register(
            id=env_id,
            entry_point="dmc2gymnasium.wrappers:DMCWrapper",
            kwargs=dict(
                domain_name=domain_name,
                task_name=task_name,
                task_kwargs=task_kwargs,
                environment_kwargs=environment_kwargs,
                visualise_reward=visualise_reward,
                from_pixels=from_pixels,
                height=height,
                width=width,
                camera_id=camera_id,
                frame_skip=frame_skip,
                channels_first=channels_first,
            ),
            max_episode_steps=max_episode_steps,
        )
    return gymnasium.make(env_id)
