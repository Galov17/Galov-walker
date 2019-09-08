import logging

from gym.envs.registration import register



logger = logging.getLogger(__name__)

register(

    id='Galov-walker-v0',

    entry_point='gym_galovwalker.envs:GalovWalkerEnv',
    
    nondeterministic = True,
)
