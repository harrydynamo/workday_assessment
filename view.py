class View:

    # return formatted result to display on output console 
    def get_result(self, candidate):
        result = f"Hello {candidate.name},\n"
        if (len(candidate.work_experience) == 0):
            result += "No Work Experience\n"
        
        for job in candidate.work_experience:
            result += f"Worked as: {job['role']}, From {job['start_date'].strftime('%b/%d/%Y')} To {job['end_date'].strftime('%b/%d/%Y')} in {job['location']}. "
            if 'gap' in job:
                result += f"Gap in CV for {job['gap']} days\n"
            else:
                result += '\n'

        return result

    # Return formatted result to save in the output file ('output/result.json')
    def get_json_output(self, candidate):
        result = {
            "name": candidate.name,
            "work_experience": []
        }
        for job in candidate.work_experience:
            job_entry = {
                "role": job['role'],
                "start_date": job['start_date'].strftime('%Y-%m-%d'),
                "end_date": job['end_date'].strftime('%Y-%m-%d'),
                "location": job['location']
            }
            if 'gap' in job:
                job_entry["gap"] = f"{job['gap']} days"
            result['work_experience'].append(job_entry)
        return result

