from config import SimulationConfig
from simulator.simulator import OilWellSimulator


def main():

    simulator = OilWellSimulator(
        SimulationConfig.default()
    )

    simulator.reset()

    for choke in [30, 35, 40, 45, 50, 55, 60]:

        simulator.step(choke)

    history = simulator.get_history()

    print()

    print("States Recorded :", len(history))

    print()

    print("Flow History")

    print(history.get_flows())

    print()

    print("Choke History")

    print(history.get_chokes())


if __name__ == "__main__":
    main()