import json
import Constants

# This is controller class.
# This class control the flow between model.py and view.py
class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    # 1. Display output on Console.
    # 2. Save the result in output file.
    def run(self):
        self.model.fetch_data()
        self.show_experience()
        print(Constants.divider)
        self.save_data()

    # Display candidates info on Console
    def show_experience(self):
        for candidate in self.model.candidates:
            info = self.view.get_result(candidate)
            print(info)

    # Save result in output/result.json
    def save_data(self):

        # Output file path
        output_file_path = Constants.output_dir_path + '/result.json'
        result = []
        for candidate in self.model.candidates:
            result.append(self.view.get_json_output(candidate))

        # Save output in result.json using write mode.
        with open(output_file_path, 'w') as json_file:
            json.dump(result, json_file, indent=4)
        
        print(f'Data saved in {output_file_path}')
