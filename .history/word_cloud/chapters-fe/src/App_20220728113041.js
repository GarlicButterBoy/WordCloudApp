import logo from './logo.svg';
import './App.css';
import React, { Component, Fragment } from "react";
import Header from './components';

class App extends Component {
  render() {
    return (
      <Fragment>
        <Header />
        <Home />
      </Fragment>
    );
  }
}

export default App;
