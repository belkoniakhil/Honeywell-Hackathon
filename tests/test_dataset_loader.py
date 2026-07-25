from utils.data_loader import DatasetLoader


loader = DatasetLoader("data/well_data.csv")

print()

for choke in [30, 35, 40, 45, 50, 55, 60, 65]:

    print(
        f"{choke}%"
        f"  Flow={loader.flow(choke):.2f}"
        f"  WHP={loader.whp(choke):.2f}"
        f"  FLP={loader.flp(choke):.2f}"
        f"  BHP={loader.bhp(choke):.2f}"
    )