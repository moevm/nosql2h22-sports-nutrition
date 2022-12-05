import { FilterEmployeesCriteria, isObjEmpty } from "../../api/branch";
import * as React from "react";
import { useEffect, useState } from "react";
import { Box, IconButton, TextField, Typography } from "@mui/material";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import { regexPhone } from "../../api/constants";

export function FindEmployeesDialog({ onChange, value }: {
                                      onChange: (val: FilterEmployeesCriteria) => void,
                                      value: FilterEmployeesCriteria
                                    }
) {

  const [curValue, setCurValue] = useState<FilterEmployeesCriteria>(value);

  useEffect(() => {
    setCurValue(value);
  }, [value]);

  const updateField = (field: string, data: string) => {
    const copy: FilterEmployeesCriteria = { ...curValue };

    if (["_id", "role", "phone_number", "name",
      "employment_date_from", "employment_date_to",
      "salary_from", "salary_to", "surname", "patronymic",
      "dismissal_date_from", "dismissal_date_to"].indexOf(field) >= 0) {
      // @ts-ignore
      copy[field] = data.length ? data : undefined;
    }
    setCurValue(copy);
  };

  return (
    <Box sx={{ width: "60%" }}>
      <Typography variant="h5">
        Filter employees
      </Typography>
      <DialogContent dividers>
        <TextField
          margin="dense"
          id="role"
          label="Role"
          fullWidth
          onChange={(val) =>
            updateField("role", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Surname"
          fullWidth
          onChange={(val) =>
            updateField("surname", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Name"
          fullWidth
          onChange={(val) =>
            updateField("name", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="salary_from"
          label="Salary from"
          fullWidth
          onChange={(val) =>
            updateField("salary_from", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="salary_to"
          label="Salary to"
          fullWidth
          onChange={(val) =>
            updateField("salary_to", val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <IconButton
          onClick={() => onChange(curValue)}
          disabled={isObjEmpty(curValue) ||
            Number(curValue.salary_from) > Number(curValue.salary_to)}
          color="inherit" title="Find stocks"
          style={{ width: "2em", margin: "10px" }}>
          <SearchOutlinedIcon />
        </IconButton>
      </DialogActions>
    </Box>
  );
}