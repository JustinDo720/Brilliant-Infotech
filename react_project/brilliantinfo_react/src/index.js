import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';
import  Demo from './Demo';
import { Upper } from './Upper';
import { API } from './API'
import { App } from "./App"
import { Provider } from 'react-redux';
import Calculator from './Cal'
import store from './store';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <Demo demo_val={ true }></Demo>
    <Upper my_str='my lowercase string'></Upper> */}
    <Provider store={store}>
      {/* <API></API>
      <App></App> */}
      <Calculator></Calculator>
    </Provider>
   
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
