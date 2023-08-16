import os
import pandas as pd
import sys

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error_message = "Error occurred in python script\nname: {0}\nLine number: {1}\nError message: {2}".format(
        filename, lineno, error
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message

class FetchData:
    def __init__(self) -> None:
        self.__data_directory = "DSPackage/Data"  # Directory where CSV files are stored
    
    def load_data(self, file_name: str):
        file_name = file_name.lower() + '.csv'
        self.__file_path = os.path.join(self.__data_directory, file_name)
        try:
            df = pd.read_csv(self.__file_path)
            print(f"The file '{file_name}' exists in the '{self.__data_directory}' directory.") 
            return df
        except FileNotFoundError as e:
            files = os.listdir(self.__data_directory)
            file_names = [item for item in files if os.path.isfile(os.path.join(self.__data_directory, item))]
            raise CustomException(f"The file '{file_name}' does not exist in the package. The available files are {file_names} ", sys)

# Example usage
try:
    fd = FetchData()
    df = fd.load_data('irikik')
except CustomException as e:
    print(f"Custom Error: {e}")
