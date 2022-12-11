import {Stack, TextField, Typography} from "@mui/material";
import * as React from "react";
import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import {getEmployeeById} from "../../api/employee";
import {NotFound} from "../NotFound";

export const EmployeePage = () => {
  const params = useParams();
  const [employee, setEmployee] = useState<any>(undefined);

  useEffect(() => {
    getEmployeeById(params.id!)
      .then((response) => response.json())
      .then((json) => {
        setEmployee(json.result[0]);
      });
  }, [params, getEmployeeById]);

  if (!employee) {
    return <NotFound />;
  }

  return (
    <Stack spacing={2}>
      <Typography variant={"h5"}> Employee {employee.surname} {employee.name}
      </Typography>
      <TextField
        style={{ width: "80%" }}
        label="Id"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee._id}
      />
      <TextField
        style={{ width: "80%" }}
        label="Surname"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.surname}
      />
      <TextField
        style={{ width: "80%" }}
        label="Name"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.name}
      />
      <TextField
        style={{ width: "80%" }}
        label="Patronymic"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.patronymic}
      />
      <TextField
        style={{ width: "80%" }}
        label="City"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.city}
      />
      <TextField
        style={{ width: "80%" }}
        label="Passport"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.passport}
      />
      <TextField
        style={{ width: "80%" }}
        label="Phone"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.phone}
      />
      <TextField
        style={{ width: "80%" }}
        label="Role"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.role}
      />
      <TextField
        style={{ width: "80%" }}
        label="Employment date"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.employment_date}
      />
      <TextField
        style={{ width: "80%" }}
        label="Salary"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={employee.salary}
      />
    </Stack>
  );
};