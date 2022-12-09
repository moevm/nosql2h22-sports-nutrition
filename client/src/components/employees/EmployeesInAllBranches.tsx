import * as React from "react";
import { useCallback, useState } from "react";
import { Box, TextField, Typography } from "@mui/material";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { findEmployee } from "api/employee";
import { EmployeesList } from "./EmployeesList";
import { FilterEmployeesCriteria, isObjEmpty } from "../../api/branch";
import { FindEmployeeContent } from "./FindEmployeeContent";
import { updateField } from "./util";

const EMPLOYEES_NOT_FOUND = "Employees not found";
export function EmployeeInAllBranches() {

  const [curValue, setCurValue] = useState<FilterEmployeesCriteria>({});

  const [employees, setEmployees] = useState([]);
  const [error, setError] = useState("");

  const getEmployee = useCallback(() => {
    findEmployee(curValue)
      .then((response) => response.ok ? response.json() : undefined)
      .then((json) => {
        setError(json ? "" : EMPLOYEES_NOT_FOUND)
        setEmployees(json ? json.result : undefined);
      })
      .catch((e) => {
        setError(e.message + ". " + EMPLOYEES_NOT_FOUND);
        setEmployees([]);
      }
  );
  }, [curValue, findEmployee]);

  return (
    <Box>
      <Box width="70%">
        <Typography variant="h5">
          Find employee in all branches
        </Typography>
        <FindEmployeeContent updateField={updateField} curVal={curValue} setCurVal={setCurValue} />
        <DialogActions>
          <Button autoFocus onClick={getEmployee}
                  disabled={isObjEmpty(curValue) ||
            Number(curValue.salary_from) > Number(curValue.salary_to)}>
            Find
          </Button>
        </DialogActions>
      </Box>
      {error.length ? <Typography> ERROR: {error}</Typography> : null}
      {employees.length ? <EmployeesList employees={employees} /> : null}
    </Box>
  );
}
