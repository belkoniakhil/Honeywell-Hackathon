from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfig:

    # Simulation
    time_step: float
    simulation_time: float
    random_seed: int
    enable_noise: bool

    # Choke
    min_choke: float
    max_choke: float
    max_choke_change: float

    # Flow
    min_flow: float
    max_flow: float

    # Pressure
    min_whp: float
    max_whp: float

    min_flp: float
    max_flp: float

    min_bhp: float
    max_bhp: float

    # Dynamics
    flow_time_constant: float
    pressure_time_constant: float

    # Initial State
    initial_flow: float
    initial_whp: float
    initial_flp: float
    initial_bhp: float
    initial_choke: float

    @classmethod
    def default(cls):

        return cls(

            # Simulation
            time_step=1.0,
            simulation_time=300.0,
            random_seed=42,
            enable_noise=False,

            # Choke
            min_choke=0.0,
            max_choke=100.0,
            max_choke_change=5.0,

            # Flow
            min_flow=0.0,
            max_flow=200.0,

            # Pressure
            min_whp=200.0,
            max_whp=300.0,

            min_flp=150.0,
            max_flp=200.0,

            min_bhp=2800.0,
            max_bhp=3200.0,

            # Dynamics
            flow_time_constant=8.0,
            pressure_time_constant=10.0,

            # Initial State
            initial_flow=92.57,
            initial_whp=262.20,
            initial_flp=186.12,
            initial_bhp=3080.59,
            initial_choke=30.0,
        )