import pandas as pd
import glob


def dataset_helper(type:str):
    if type == "train":
        # Load the problems

        for file_name in glob.glob("datasets/train/*.wclq"):
            pd.read_csv(file_name,sep=" ", skiprows=1)
            pass
        #Load the solutions
        for file_name in glob.glob("datasets/train/*.sol"):
            pass



















def test():
    df = pd.read_csv("datasets/C1000-9.mtx",prefix="V",sep=" ",skiprows=2)







if __name__ == '__main__':
    test()