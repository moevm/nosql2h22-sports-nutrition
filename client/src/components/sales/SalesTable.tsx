import {HOST} from "../../constants";
import * as React from "react";

interface SalesTableProps {
    sales: any[];
    forPagination?: boolean;
}

export const SalesTable = (props: SalesTableProps) => {
    const {sales, forPagination} = props;
    return (
        <table>
            <thead>
            <tr>
                <th>Sale Id</th>
                <th>Price</th>
                <th>Amount</th>
                 <th>Branch Id</th>
                <th>Product Id</th>
            </tr>
            </thead>
            <tbody>
            {sales.map((item) => {
                return (
                    <tr key={item._id}>
                        <td>item._id</td>
                        <td>item.price</td>
                        <td>item.amount</td>
                        <td>item.date</td>
                    </tr>
                );
            })}
            </tbody>
        </table>
    )
}