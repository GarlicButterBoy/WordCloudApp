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
                        <th>Started</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {!students || students.length <= 0 ? (
                        <tr>
                            
                        </tr>
                    )}
                </tbody>
            </Table>
        );
    }
}