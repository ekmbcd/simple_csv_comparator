import pandas as pd
import matplotlib.pyplot as plt
import argparse


def plot_csv(filename, filename2):
    # Read the CSV file
    data = pd.read_csv(filename)

    # Use the index for the x-axis and the first three columns for the y-axis
    x = data.index
    y1 = data.iloc[:, 0]
    y2 = data.iloc[:, 1]

    # Create the plot
    plt.plot(x, y1, label="Objective")
    plt.plot(x, y2, label=filename)
    plt.plot(x, y1 - y2, label="Difference")

    # ignore first 10% and last 10% of the data
    objective_short = y1[int(len(y1) * 0.1) : int(len(y1) * 0.9)]
    filename_short = y2[int(len(y2) * 0.1) : int(len(y2) * 0.9)]

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
        data2 = pd.read_csv(filename2)
        y2 = data2.iloc[:, 1]
        plt.plot(x, y2, label=filename2)

        filename_short = y2[int(len(y2) * 0.1) : int(len(y2) * 0.9)]

        print(
            f"Total error of {filename2} is: ",
            sum(abs(filename_short - objective_short)),
        )
        print(
            f"The maximum error of {filename2} is: ",
            max(abs(filename_short - objective_short)),
        )
        print(
            "Mean error of ",
            filename2,
            " is: ",
            sum(abs(filename_short - objective_short)) / len(filename_short),
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
