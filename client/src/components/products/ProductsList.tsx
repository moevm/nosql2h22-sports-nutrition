import {Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@mui/material";
import React from "react";

export const ProductsList = ({ products, ofAllSuppliers }:
                               {
                                 products: any[];
                                 ofAllSuppliers?: boolean
                               }) => {
  if (!products.length) {
    return <p> No products yet </p>;
  }
  return (
    <TableContainer component={Paper}>
      <Table sx={{ maxWidth: 650 }}>
        <TableHead>
          <TableRow>
            <TableCell>Id</TableCell>
            <TableCell>Descriptor id</TableCell>
            {ofAllSuppliers ? (<TableCell>Supplier id</TableCell>) : null}
            <TableCell align="right">Name</TableCell>
            <TableCell align="right">Price</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {products.map((row) => (
            <TableRow
              key={row._id}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row._id}
              </TableCell>
              <TableCell component="th" scope="row">
                {row.descriptor._id}
              </TableCell>
              {ofAllSuppliers ?
                <TableCell component="th" scope="row">
                  {row.supplier_id}
                </TableCell> : null}
              <TableCell align="right">{row.descriptor.name}</TableCell>
              <TableCell align="right">{row.price}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};
