import React, { useState }  from 'react';  
import axios from "axios";
import './App.css';

function App() {

  const [classifyData, setClassifyData] = useState(null);
  const [file, setFile] = useState(null);

  const handleFileChange = event => {
    setFile(event.target.files[0]);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('image', file);
    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      // Assuming the Flask server returns the URL of the uploaded image in the "url" field of the JSON response
      const imageUrl = data.url;
      
      // Set the src attribute of an img element to display the uploaded image
      const imageElement = document.getElementById('uploaded-image');
      imageElement.src = imageUrl;
    })
      .catch(error => {
        console.log("error")
      });
  };

  function getData(){
    axios({
      method: "GET",
      url: "/main",
    })
    .then((response) => {
      const res = response.data
      setClassifyData(({
        image_prediction: res.name,
        // accuracy_percentage: res.about
      }))
    }).catch((error) => {
      if (error.response){
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
      }
  })}
  

  return (
    <div className="App">
        {/* <input name="img" type="file" onChange={handleFileChange}></input>
        <button type="button" onClick={handleUpload}>Upload</button> */}
        <button type="button" onClick={getData}>Compute</button>
      {classifyData && <div>
            <p>Prediction: {classifyData.image_prediction}</p>
          </div>
      }      
    </div>
  );
}

export default App;
