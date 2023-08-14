import pandas as pd
import os

class FetchData:
    def __init__(self) -> None:
        self.__file_path = ""
    
    def load_data(self, file_name: str):
        file_name = file_name.lower() + '.csv'
        self.__file_path= os.path.join("Data", file_name)
        try:
            df= pd.read_csv(self.__file_path)
            print(f"The file '{file_name}' exists in the '{self.__file_path}' directory.") 
            return df
        except FileNotFoundError:
            print(f"The file '{file_name}' does not exist in the '{self.__file_path}' directory.")