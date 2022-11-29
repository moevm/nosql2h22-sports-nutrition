import * as React from "react";
import { useCallback, useState } from "react";
import { Box, TextField, Typography } from "@mui/material";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { findEmployee } from "api/employee";
import { EmployeesList } from "./EmployeesList";

export function FindEmployeeInAllBranches() {

  const [id, setId] = useState("");
  const [employee, setEmployee] = useState(undefined);
  const [isClicked, setIsClicked] = useState(false);

  const getEmployee = useCallback(() => {
    setIsClicked(true);
    findEmployee(id)
      .then((response) => response.ok ? response.json() : undefined)
      .then((json) => {
        setEmployee(json ? json : undefined);
      });
  }, [id, findEmployee]);

  return (
    <Box>
      <Box width="70%">
        <Typography variant="h5">
          Find employee in all branches
        </Typography>
        <DialogContent dividers>
          <TextField
            margin="dense"
            id="id"
            label="Enter employee's id"
            fullWidth
            onChange={(val) =>
              setId(val.target.value)}
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button autoFocus onClick={getEmployee}
                  disabled={!id.length}>
            Find
          </Button>
        </DialogActions>
      </Box>
      {employee && <EmployeesList employees={[employee]} />}
    </Box>
  );
}
