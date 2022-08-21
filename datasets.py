import pandas as pd
import glob


def read_node_values(type):
    if type == "train":
        for file_name in glob.glob("datasets/train/*.wclq"):
            df = pd.read_csv(file_name, sep=" ", skiprows=1, names=["type", "v1", "v2", "v3"])
            nodes = df[df["type"] == "v"]
            nodes = edges.drop(["type", "v3"], axis=1)
            #edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")

            pass
            # Load the solutions
        for file_name in glob.glob("datasets/train/*.sol"):
            pass


def to_edgelist(type):
    if type == "train":
        # Load the problems

        for file_name in glob.glob("datasets/train/*.wclq"):
            df = pd.read_csv(file_name, sep=" ", skiprows=1, names=["type", "v1", "v2", "v3"])
            edges = df[df["type"] == "e"]
            edges = edges.drop(["type", "v3"], axis=1)
            edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")

            pass
        # Load the solutions
        for file_name in glob.glob("datasets/train/*.sol"):
            pass


def test():
    df = pd.read_csv("datasets/C1000-9.mtx", prefix="V", sep=" ", skiprows=2)


if __name__ == '__main__':
    to_edgelist("train")
