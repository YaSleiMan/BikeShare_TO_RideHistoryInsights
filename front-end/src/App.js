import React, { useState } from "react";
import axios from "axios";

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [resultText, setResultText] = useState("");
  const [resultImage1, setResultImage1] = useState("");
  const [resultImage2, setResultImage2] = useState("");
  const [resultImage3, setResultImage3] = useState("");
  const [resultHTML, setResultHTML] = useState("");

  const handleRun = () => {
    // Make a POST request to the Python backend
    axios
      .post("/run", { username, password, startDate, endDate })
      .then((response) => {
        const data = response.data;

        setResultText(data.result_text);
        setResultImage1(data.result_image1);
        setResultImage2(data.result_image2);
        setResultImage3(data.result_image3);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  const handleShowHTML = (htmlChoice) => {
    // Make a POST request to the Python backend to get the selected HTML template
    axios
      .post("/show_html", { html_choice: htmlChoice })
      .then((response) => {
        setResultHTML(response.data);
      })
      .catch((error) => {
        console.error("Error fetching HTML:", error);
      });
  };

  return (
    <div>
      <h1>Run Your Code Online</h1>
      <label>
        Username:
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </label>
      <label>
        Password:
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </label>
      <label>
        Start Date:
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />
      </label>
      <label>
        End Date:
        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </label>
      <button onClick={handleRun}>Run</button>

      <h2>Result Text:</h2>
      <p>{resultText}</p>

      <h2>Result Images:</h2>
      <div className="image-container">
        <img src={resultImage1} alt="Image 1" />
        <img src={resultImage2} alt="Image 2" />
        <img src={resultImage3} alt="Image 3" />
      </div>

      <h2>Select Result HTML:</h2>
      <select onChange={(e) => handleShowHTML(e.target.value)}>
        <option value="">--Select HTML--</option>
        <option value="html_template1.html">HTML Template 1</option>
        <option value="html_template2.html">HTML Template 2</option>
        <option value="html_template3.html">HTML Template 3</option>
      </select>

      <h2>Result HTML:</h2>
      <div dangerouslySetInnerHTML={{ __html: resultHTML }}></div>
    </div>
  );
};

export default App;
