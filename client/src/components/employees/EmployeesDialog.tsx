import {isObjEmpty} from "../../api/branch";
import * as React from "react";
import {useEffect, useState} from "react";
import {Box, IconButton, Typography} from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import {FindEmployeeContent} from "./FindEmployeeContent";
import {updateField} from "./util";
import {FilterEmployeesCriteria} from "../../api/employee";

interface FindEmployeeProps {
  onChange: (val: FilterEmployeesCriteria) => void,
  value: FilterEmployeesCriteria
}

export function EmployeesDialog({ onChange, value }: FindEmployeeProps) {

  const [curValue, setCurValue] = useState<FilterEmployeesCriteria>(value);

  useEffect(() => {
    setCurValue(value);
  }, [value]);

  return (
    <Box sx={{ width: "60%" }}>
      <Typography variant="h5">
        Employees
      </Typography>
      <FindEmployeeContent updateField={updateField} curVal={curValue} setCurVal={setCurValue} />
      <DialogActions>
        <IconButton
          onClick={() => {
            onChange(curValue)}}
          disabled={isObjEmpty(curValue)}
          color="inherit" title="Find stocks"
          style={{ width: "2em", margin: "10px" }}>
          <SearchOutlinedIcon />
        </IconButton>
      </DialogActions>
    </Box>
  );
}