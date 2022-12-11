import {Stack} from "@mui/material";
import * as React from "react";

interface IProps {
  suppliers: any[];
  pagination: boolean;
}

export const SuppliersTable = ({ suppliers, pagination }: IProps) => {
  return (
    <table>
      <thead>
      <tr>
        <th>Supplier Id</th>
        <th>Name</th>
        <th>Products</th>
      </tr>
      </thead>
      <tbody>
      {suppliers.map((item) => {
        return (
          <tr key={item._id} className="suppliers-table">
            <td className="cell-id">
              <a href={`/supplier/${item._id}`}>
                {item._id}
              </a></td>
            <td>{item.name}</td>
            <td>
              <Stack>
                {pagination ?
                  item.products.join(", ") + "..." :
                  item.products.map((pr: any) => pr.descriptor.name).slice(0, 3).join(", ") + "..."}
              </Stack>
            </td>
          </tr>
        );
      })}
      </tbody>
    </table>
  );
};