from model import Model
from view import View
from controller import Controller
from pathlib import Path
import Constants

# This class will make the data and ouput directory in the current working directory.
class Driver:

    def __init__(self):
        self.make_dir(Constants.data_dir_path)
        self.make_dir(Constants.output_dir_path)
        print(Constants.divider)

    # make directories for data and output
    def make_dir(self, path):
        dir_path = Path(path)
        try:
            dir_path.mkdir()
            print(f"** Directory '{dir_path}' created successfully **")
        except FileExistsError:
            print(f"** Directory '{dir_path}' already exists **")
        except OSError as error:
            print(f"** Error creating directory '{dir_path}': {error} **")

if __name__ == "__main__":
    driver = Driver()

    path = Constants.data_dir_path + "/data.json"
    
    model = Model(path)
    view = View()
    controller = Controller(model, view)
    controller.run()

