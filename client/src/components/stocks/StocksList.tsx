import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";
import React from "react";
import {HOST} from "../../constants";

export const StocksList = ({ stocks }: { stocks: any[] }) => {
  if (!stocks.length) {
    return <p> No stocks in this branch </p>;
  }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ maxWidth: 650 }}>
        <TableHead>
          <TableRow>
            <TableCell>Id</TableCell>
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Price</TableCell>
            <TableCell align="right">Amount</TableCell>
            <TableCell align="right">Supplier</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {stocks.map((row) => (
            <TableRow
              key={row._id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row._id}
              </TableCell>
              <TableCell align="right">{row.product.descriptor.name}</TableCell>
              <TableCell align="right">{row.price}</TableCell>
              <TableCell align="right">{row.amount}</TableCell>
              <TableCell align="right"> <a href={`${HOST}8080/supplier/${row.product.supplier_id}`}>
                {row.product.supplier_id}
              </a></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};