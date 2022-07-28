import React, { Component } from "react";
import { Table } from "reactstrap";
import NewChapterModal from "./NewChapterModal";
import ConfirmRemovalModal from './ConfirmRemovalModal';

class ChapterList extends Component {
    render() {
        const students = this.props.students;
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>Book</th>
                        <th>Words</th>
                        <th></th>
                    </tr>
                </thead>
            </Table>
        );
    }
}