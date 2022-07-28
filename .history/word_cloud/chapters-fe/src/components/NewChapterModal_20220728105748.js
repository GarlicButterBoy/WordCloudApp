import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewChapterForm from "./NewChapterForm";

class NewChapterModal extends Component {
  state = {
    modal: false,
  };

  toggle = () => {
    this.setState((previous) => ({
      modal: !previous.modal,
    }));
  };

  render() {
    const create = this.props.create;
    let title = "Editing Chapter";
    let button = <Button onClick={this.toggle}>Edit</Button>;

    if (create) {
      title = "Creating New Chapter";
      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Create
        </Button>
      );
      }
      
      
  }
}
