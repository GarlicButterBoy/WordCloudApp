import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import ChapterList from "./ChapterList";
import NewChapterModal from "./NewChapterModal";
import axios from "axios";
import { API_URL } from "../constants";

class Home extends Component {
  state = {
    chapters: [],
  };

  componentDidMount() {
    this.resetState();
  }

  getChapters = () => {
    axios.get(API_URL).then((res) => this.setState({ chapters: res.data }));
    };
    
    resetState = () => {
        this.getChapters();
    };
}
