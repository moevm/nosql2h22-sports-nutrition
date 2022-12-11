import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import * as React from "react";
import { useState } from "react";
import { FilterEmployeesCriteria } from "../../api/branch";
import { toServerDateFormat } from "../../api/functions";

interface FindEmployeeContentProps {
  updateField: (name: string, value: string, curValue: FilterEmployeesCriteria,
                setCurValue: (val: FilterEmployeesCriteria) => void) => void;
  curVal: FilterEmployeesCriteria;
  setCurVal: (val: FilterEmployeesCriteria) => void;
}

export const FindEmployeeContent = (props: FindEmployeeContentProps) => {
  const { updateField, curVal, setCurVal } = props;
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
          updateField("salary_from", val.target.value, curVal, setCurVal);
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
            setHelperText("Salary_from must be less then salary_to!");
          } else {
            updateField("salary_to", val.target.value, curVal, setCurVal);
            setHelperText("");
          }
        }
        }
        variant="standard"
        helperText={helperText}
      />
      <label style={{ marginTop: "5px" }} htmlFor={"employment-date-from"}>
        Employment date from
      </label>
      <input
        style={{ width: "100%" }}
        type="datetime-local"
        id="employment_date-from"
        placeholder="dd/mm/yyyy"
        min="2010-01-01T00:00"
        max="2023-12-31T00:00"
        onChange={(val) => {
          updateField("employment_date_from", toServerDateFormat(val.target.value), curVal, setCurVal);
        }
        }
      />
      <label style={{ marginTop: "5px" }} htmlFor={"employment-date-to"}>
        Employment date to
      </label>
      <input
        required
        style={{ width: "100%" }}
        type="datetime-local"
        id="employment_date_to"
        placeholder="dd/mm/yyyy"
        min="2010-01-01T00:00"
        max="2023-12-31T00:00"
        onChange={(val) => {
          updateField("employment_date_to", toServerDateFormat(val.target.value), curVal, setCurVal);
        }
        }
      />
    </DialogContent>
  );
};