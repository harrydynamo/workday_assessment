import json
# import requests # type: ignore
from datetime import datetime
import Constants

class Candidate:

    # Initialize name and work experience of the candidate
    def __init__(self, name, work_experience):
        self.name = name
        self.work_experience = work_experience

    # Calculate gaps of the candidate.
    def calculate_gaps(self):
        self.work_experience.sort(reverse = True, key = lambda x: x["start_date"])
        for i in range(1, len(self.work_experience)):
            current_job_end = self.work_experience[i]['end_date']
            next_job_start = self.work_experience[i-1]['start_date']
            gap = (next_job_start - current_job_end).days
            if gap > 1:
                self.work_experience[i-1]['gap'] = gap

    # toString implementation of Candidate
    # eg -
    #   Name: Walter White
    #   Work Experience: []
    def __str__(self):
        return f'Name: {self.name}\nWork Experience: {self.work_experience}'

# This class is used to used to fetch and parse the data.
class Model:
    
    def __init__(self, path):
        self.path = path
        self.candidates = []

    def fetch_data_from_url(self, url):
        # try:
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()

            # Save the JSON data to a file
            with open(Constants.data_dir_path+'/data.json', 'w') as file:
                json.dump(json_data, file, indent=4)

        return response.status_code
                
        # except Exception:
        #     print('Internet Connection Error')
        # return -1

    def fetch_data(self):
        try:
            with open(self.path, 'r') as f:
                data = json.load(f)
            self.parse_data(data)
        except FileNotFoundError:
            print('data.json file does not exist.')
            url = Constants.url

            # response = self.fetch_data_from_url(url)
            # if (response == 200):
                # print(f"JSON data has been saved to {Constants.data_dir_path + '/data.json'}")
                # self.fetch_data()
            # else:
            #   print(f"Failed to fetch data. HTTP Status code: {response}")
            print(Constants.divider)

    def parse_data(self, data):
        for candidate_data in data:
            name = candidate_data['contact_info']['name']['formatted_name']
            work_experience = []

            for job in candidate_data['experience']:
                start_date = datetime.strptime(job['start_date'], "%b/%d/%Y")
                end_date = datetime.strptime(job['end_date'], "%b/%d/%Y")
                role = job['title']
                location = job['location']['short_display_address']
                work_experience.append({
                    'start_date': start_date,
                    'end_date': end_date,
                    'role': role,
                    'location': location
                })
            
            candidate = Candidate(name, work_experience)
            candidate.calculate_gaps()
            self.candidates.append(candidate)

