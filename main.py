from config import SimulationConfig
from simulator.simulator import OilWellSimulator


def main():

    config = SimulationConfig.default()

    simulator = OilWellSimulator(config)

    state = simulator.reset()

    print("\nInitial State\n")
    print(state)

    print("\nRunning Simulation\n")

    for i in range(20):

        state = simulator.step(60)

        print(state)


if __name__ == "__main__":
    main()