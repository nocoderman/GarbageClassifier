import React, { useState }  from 'react';  
import axios from "axios";
import './App.css';

function App() {

  const [classifyData, setClassifyData] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileInput = (event) => {
    setSelectedFile(event.target.files[0]);
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
        // console.log(data.filename);
        setClassifyData(({
          image_prediction: data.result,
          // accuracy_percentage: res.about
        }))
        console.log(data.result);
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
      <form onSubmit={handleFormSubmit}>
        <input type="file" onChange={handleFileInput} />
        <button type="submit">Upload</button>
      </form>
      {selectedFile && <img className="temp-img" src={URL.createObjectURL(selectedFile)} alt="Selected Image" />}
      {(classifyData) && <div>
      <p>Prediction: {classifyData.image_prediction}</p>
      </div>}  
    </div>



  );
}

export default App;
