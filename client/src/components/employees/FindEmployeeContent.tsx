import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import * as React from "react";
import { FilterEmployeesCriteria } from "../../api/branch";
import { useState } from "react";

interface FindEmployeeContentProps {
  updateField: (name: string, value: string, curValue: FilterEmployeesCriteria,
                setCurValue: (val: FilterEmployeesCriteria) => void) => void;
  curVal: FilterEmployeesCriteria;
  setCurVal: (val: FilterEmployeesCriteria) => void;
}

export const FindEmployeeContent = (props: FindEmployeeContentProps) => {
  const {updateField, curVal, setCurVal} = props;
  const [helperText, setHelperText] = useState("");
  return (
  <DialogContent dividers>
    <TextField
      margin="dense"
      id="id"
      label="Id"
      fullWidth
      onChange={(val) =>
        updateField("_id", val.target.value, curVal, setCurVal)}
      variant="standard"
    />
    <TextField
      margin="dense"
      id="role"
      label="Role"
      fullWidth
      onChange={(val) =>
        updateField("role", val.target.value, curVal, setCurVal)}
      variant="standard"
    />
    <TextField
      margin="dense"
      id="name"
      label="Surname"
      fullWidth
      onChange={(val) =>
        updateField("surname", val.target.value, curVal, setCurVal)}
      variant="standard"
    />
    <TextField
      margin="dense"
      id="name"
      label="Name"
      fullWidth
      onChange={(val) =>
        updateField("name", val.target.value, curVal, setCurVal)}
      variant="standard"
    />
    <TextField
      margin="dense"
      id="patronymic"
      label="Patronymic"
      fullWidth
      onChange={(val) =>
        updateField("patronymic", val.target.value, curVal, setCurVal)}
      variant="standard"
    />
    <TextField
      margin="dense"
      id="salary_from"
      label="Salary from"
      fullWidth
      onChange={(val) => {
        updateField("salary_from", val.target.value, curVal, setCurVal)
      }
      }
      variant="standard"
    />
    <TextField
      margin="dense"
      id="salary_to"
      label="Salary to"
      fullWidth
      onChange={(val) => {
        if (Number(curVal.salary_from) > Number(val.target.value)) {
          setHelperText("Salary_from must be less then salary_to!")
        }
        else {
          updateField("salary_to", val.target.value, curVal, setCurVal);
          setHelperText("");
        }
      }
      }
      variant="standard"
      helperText={helperText}
    />
  </DialogContent>
)
};