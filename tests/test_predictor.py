from config import SimulationConfig
from simulator.simulator import OilWellSimulator
from controller.predictor import Predictor


simulator = OilWellSimulator(
    SimulationConfig.default()
)

predictor = Predictor(
    simulator.flow_model
)

state = simulator.reset()

print()

for choke in [30, 35, 40, 45, 50, 55, 60]:

    flow = predictor.predict_flow(
        state,
        choke,
    )

    print(
        f"Choke={choke}%"
        f"  Predicted Flow={flow:.2f}"
    )