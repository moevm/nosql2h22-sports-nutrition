import { Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow } from "@mui/material";
import React from "react";

export const EmployeesList = ({ employees}: {employees: any[]}) => {
  if (!employees.length) {
    return <p> No employees in this branch </p>;
  }
    return (
      <TableContainer component={Paper}>
        <Table sx={{ maxWidth: 650 }}>
          <TableHead>
            <TableRow>
              <TableCell>Id</TableCell>
              <TableCell align="right">Name</TableCell>
              <TableCell align="right">Role</TableCell>
              <TableCell align="right">Phone</TableCell>
              <TableCell align="right">Salary</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {employees.map((row) => (
              <TableRow
                key={row._id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row._id}
                </TableCell>
                <TableCell align="right">{row.surname + " " + row.name + " "+ row.patronymic}</TableCell>
                <TableCell align="right">{row.role}</TableCell>
                <TableCell align="right">{row.phone}</TableCell>
                <TableCell align="right">{row.salary}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    );
};