import { useState } from 'react'
import React, { Component }  from 'react';  
import axios from "axios";
import './App.css';

function App() {

  const [classifyData, setClassifyData] = useState(null)

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
        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {classifyData && <div>
              <p>Profile name: {classifyData.image_prediction}</p>
              {/* <p>About me: {classifyData.accuracy_percentage}</p> */}
            </div>
        }      
    </div>
  );
}

export default App;
