import React, { useState, useRef }  from 'react';  
import ParticlesBg from 'particles-bg';
import axios from "axios";
import './App.css';
import {FaCloudUploadAlt} from 'react-icons/fa'

function App() {

  const [classifyData, setClassifyData] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  const fileInput = useRef(null);


  const handleFileInput = (event) => {
    setSelectedFile(event.target.files[0]);
    setClassifyData(null);
  };

  const handleFormSubmit = (event) => {
    event.preventDefault();
    if (selectedFile) {
      uploadImage(selectedFile);
    }
  };



  function uploadImage(inputFile) {
    axios({
      method: "POST",
      url: "/upload",
      data: {
        file: inputFile
      },
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    .then((response) => {
      const data = response.data
      if (data.success) {
        console.log("File uploaded successfully");
        setClassifyData(({
          image_prediction: data.result,
          accuracy_percentage: data.accuracy
        }))
        console.log(data.result);
        // console.log(data.accuracy);
        // console.log(filename);
      }
    }).catch((error) => {
      if (error.response){
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
      }
    }
  )}

  return (
    <div className="App">
      <ParticlesBg type="cobweb" bg={true} />
      <div className="main-container">
        <div className="app-header">
          <p className="header-text">
            GARBAGE CLASSIFIER
          </p>
        </div>

        <div className="app-input">
          <form id="myForm" onSubmit={handleFormSubmit}>
            <label className="file-input-button">
              <div className="input-container">
                <input className="file-input" type="file" ref={fileInput} onChange={handleFileInput} style={{display:'none'}}/>
                <FaCloudUploadAlt/> 
                <p className="attach-text">Attach Image</p>
              </div>
            </label>
            {selectedFile && <img className="temp-img" src={URL.createObjectURL(selectedFile)} alt="Selected Image" />}
            {(classifyData) && <div>
            <p className="prediction-text">Prediction: {classifyData.image_prediction}</p>
            </div>}
            <button className="upload-button" type="submit">Compute Prediction</button>

          </form>

        </div>
      </div>
    </div>
  );
}

export default App;
