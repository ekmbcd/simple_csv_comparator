import pandas as pd
import matplotlib.pyplot as plt
import argparse


def plot_csv(filename, filename2):
    # Read the CSV file
    data = pd.read_csv(filename)
    data2 = None
    position2 = None
    objective2 = None

    if filename2:
        data2 = pd.read_csv(filename2)

    # Find min length of the two files
    min_length = len(data)
    if filename2:
        min_length = min(min_length, len(data2))

    # Truncate the data to the min length
    data = data[:min_length]
    if filename2:
        data2 = data2[:min_length]

    # Use the index for the x-axis and the first three columns for the y-axis
    x = data.index
    objective = data.iloc[:, 0]
    position_1 = data.iloc[:, 1]

    if filename2:
        objective2 = data2.iloc[:, 0]
        position2 = data2.iloc[:, 1]

    # Create the plot
    plt.plot(x, objective, label="Objective")
    plt.plot(x, position_1, label=filename)
    plt.plot(x, objective - position_1, label="Difference")

    if filename2:
        plt.plot(x, objective2, label="Objective2")
        plt.plot(x, position2, label=filename2)
        plt.plot(x, objective2 - position2, label="Difference2")

    # ignore first 5% and last 5% of the data
    objective_short = objective[int(len(objective) * 0.05) : int(len(objective) * 0.95)]
    filename_short = position_1[
        int(len(position_1) * 0.05) : int(len(position_1) * 0.95)
    ]

    print(f"Total error of {filename} is: ", sum(abs(filename_short - objective_short)))
    print(
        f"The maximum error of {filename} is: ",
        max(abs(filename_short - objective_short)),
    )
    print(
        "Mean error of ",
        filename,
        " is: ",
        sum(abs(filename_short - objective_short)) / len(filename_short),
    )

    if filename2:
        filename2_short = position2[
            int(len(position2) * 0.05) : int(len(position2) * 0.95)
        ]
        objective2_short = objective2[
            int(len(objective2) * 0.05) : int(len(objective2) * 0.95)
        ]

        print(
            f"Total error of {filename2} is: ",
            sum(abs(filename2_short - objective2_short)),
        )
        print(
            f"The maximum error of {filename2} is: ",
            max(abs(filename2_short - objective2_short)),
        )
        print(
            "Mean error of ",
            filename2,
            " is: ",
            sum(abs(filename2_short - objective2_short)) / len(filename2_short),
        )

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


# Create the parser
parser = argparse.ArgumentParser(description="Plot a CSV file.")

# Add the arguments
parser.add_argument("filename", type=str, help="The filename of the CSV file")
parser.add_argument(
    "filename2",
    type=str,
    help="The filename of the other file",
    nargs="?",
    default=None,
)

# Parse the arguments
args = parser.parse_args()

# Call the function with the filename
plot_csv(args.filename, args.filename2)
