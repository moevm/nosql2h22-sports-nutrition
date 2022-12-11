import {HOST} from "../../constants";
import * as React from "react";

interface BranchesTableProps {
    branches: any[];
    forPagination?: boolean;
}

export const BranchesTable = (props: BranchesTableProps) => {
    const {branches, forPagination} = props;
    return (
        <table>
            <thead>
            <tr>
                <th>Branch Id</th>
                <th>Name</th>
                <th>Location</th>
                 <th>Employees</th>
                <th>Stocks</th>
            </tr>
            </thead>
            <tbody>
            {branches.map((item) => {
                return (
                    <tr key={item._id} className="branches-table">
                        <td className="cell-id"
                        ><a href={`${HOST}8080/branch/id/${item._id}`}>
                            {item._id}
                        </a></td>
                        <td>{item.name}</td>
                        <td>{item.city}</td>
                        {forPagination ?
                            <>
                            <td>{item.employees}</td>
                            <td> {item.stocks} </td>
                                </> :
                             <>
                            <td>{item.employees.length}</td>
                            <td> {item.stocks.length} </td>
                                </> }
                    </tr>
                );
            })}
            </tbody>
        </table>
    )
}