import pandas as pd
import glob


def read_node_values(type):
    if type == "train":
        for file_name in glob.glob("datasets/train/*.wclq"):
            df = pd.read_csv(file_name, sep=" ", skiprows=1, names=["type", "v1", "v2", "v3"])
            nodes = df[df["type"] == "v"]
            nodes = edges.drop(["type", "v3"], axis=1)
            # edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")

            pass
            # Load the solutions
        for file_name in glob.glob("datasets/train/*.sol"):
            pass


def get_df_solution(type):
    if type == "train":
        for file_name in glob.glob("datasets/train/*.sol"):
            df = pd.read_csv(file_name, sep=" ", skiprows=2, names=["type", "v1", "v2", "v3"])
            edges = df[df["type"] == "e"]
            edges = edges.drop(["type", "v3"], axis=1)
            edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")


def get_list_of_files(dir, extension):
    with open(dir + "/" + extension.replace(".", "") + "_files.txt", "a") as f:
        patern = "{}/*.{}".format(dir, extension.replace(".", ""))
        for file_name in glob.glob(patern):
            f.write(file_name+"\n")


def to_edgelist(type):
    if type == "train":
        # Load the problems

        for file_name in glob.glob("datasets/train/*.wclq"):
            df = pd.read_csv(file_name, sep=" ", skiprows=1, names=["type", "v1", "v2", "v3"])
            edges = df[df["type"] == "e"]
            edges = edges.drop(["type", "v3"], axis=1)
            edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")
    else:

        # Load the graph

        for file_name in glob.glob("datasets/test/*.wclq"):
            df = pd.read_csv(file_name, sep=" ", skiprows=1, names=["type", "v1", "v2", "v3"])
            edges = df[df["type"] == "e"]
            edges = edges.drop(["type", "v3"], axis=1)
            edges.to_csv(file_name.replace("wclq", "edgelist"), index=False, header=False, sep=" ")

        # Load the solutions


def test():
    df = pd.read_csv("datasets/C1000-9.mtx", prefix="V", sep=" ", skiprows=2)


if __name__ == '__main__':
    get_list_of_files("datasets/test","edgelist")
    # to_edgelist("train")
    # to_edgelist("test")
