# Tarea: Taxi

#En grupos de tres estudiantes resuelvan el ambiente ["Taxi-v3"](https://gym.openai.com/envs/Taxi-v3/)


#- Describa detalladamente el ambiente (estados posibles, acciones posibles, recompensas, etc)
#- Utilice $\epsilon$ greedy Q-learning para entrenar un agente que resuelva el problema
#- Muestre en una gráfica la evolución de la recompensa promedio de su agente

# Cuide su salud, discutan el problema y la solución usando herramientas de teletrabajo (whereby.com, google talk, skype, slack)

from gym import wrappers
import gym 


env = gym.make("Taxi-v3")
env = wrappers.Monitor(env, './video', video_callable=lambda episode_id: True,force=True)
env.reset()
frames = []
for t in range(1000):
    #Render to frames buffer
    env.render()
    a = env.action_space.sample()
    _, _, end, _ = env.step(a)
    if end:
        break
env.close()