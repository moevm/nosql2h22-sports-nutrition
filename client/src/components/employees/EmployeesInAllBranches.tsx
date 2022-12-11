import * as React from "react";
import {useCallback, useState} from "react";
import {Box, Typography} from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import {FilterEmployeesCriteria, findEmployee} from "api/employee";
import {EmployeesList} from "./EmployeesList";
import {isObjEmpty} from "../../api/branch";
import {FindEmployeeContent} from "./FindEmployeeContent";
import {updateField} from "./util";

export function EmployeeInAllBranches() {

  const [curValue, setCurValue] = useState<FilterEmployeesCriteria>({});

  const [employees, setEmployees] = useState([]);
  const [error, setError] = useState("");

  const getEmployee = useCallback(() => {
    findEmployee(curValue)
      .then(async (response) => {
        if (response.ok) return response.json();
        else {
          const text = await response.text();
          setError(JSON.parse(text).message);
          setEmployees([]);
          return undefined;
        }
      })
      .then((json) => {
        if (json) {
          setError("");
          setEmployees(json.result);
        }
      })
      .catch((e) => {
          setError(e.message);
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
