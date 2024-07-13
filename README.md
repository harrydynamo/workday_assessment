<h3>Workday Software Developer Home Assignment.</h3>

<p><strong>Directory</strong></p>
hiredscore / </br>
&emsp; - main.py </br>
&emsp; - Constants.py </br>
&emsp; - model.py </br>
&emsp; - controller.py </br>
&emsp; - view.py </br>
&emsp; data / </br>
&emsp; &emsp; - data.json </br>
&emsp; output / </br>
&emsp; &emsp; - result.json </br>
&emsp; - README.md </br> </br>

<p><strong>Implementation Details</strong></p>
<ul>
  <li>
    <p>main.py</p>
    <p> - This is dirver class. First it initialize the directories and required objects and call the run method of controller class</p>
  </li>
  <li>
    <p>model.py</p>
    <p> - model.py will fetch data from the local directory, parse it, and process the work experience, including calculating gaps between jobs. If the data.json file does not exist it will fetch from the url and store it in data directory.</p>
  </li>

  <li>
    <p>view.py</p>
    <p> - view.py will format the processed data into a string and JSON format.</p>
  </li>

  <li>
    <p>controller.py</p>
    <p> - controller.py is used to manage the flow between model.py and view.py</p>
  </li>

  <li>
    <p>Constants.py</p>
    <p> - Constants.py contains data, output and url constants for ease of access</p>
  </li>

  <li>
    <p>data/data.json</p>
    <p> - This will store the data</p>
  </li>

  <li>
    <p>output/result.json</p>
    <p> - This will store the result in json format</p>
  </li>
</ul>

<br>
<p><strong>Steps to execute code.</strong></p>
<ul>
  <li>OS: MacOS Monterey version 12.7.4</li>
  <li>> python --version <br> Python 3.10.9</li>
  <li>> python main.py</li>
</ul>
<p>Note: After following these steps you can see the output in console and output/result.json file</p>
