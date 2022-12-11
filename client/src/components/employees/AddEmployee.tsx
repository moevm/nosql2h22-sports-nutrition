import * as React from "react";
import { useCallback, useState } from "react";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplier";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { EmployeeData, postEmployee } from "../../api/employee";
import { checkObjOnDefault, toServerDateFormat } from "../../api/functions";
import { regexLetters, regexPhone } from "api/constants";

interface AddEmployeeProps {
  isOpen: boolean;
  setOpen: (action: boolean) => void;
  branchId: string;
  employees: any[];
  setEmployees: (list: any[]) => void;
}

export const AddEmployee = ({ isOpen, setOpen, branchId, employees, setEmployees }:
                              AddEmployeeProps) => {

  const [postData, setPostData] = useState<EmployeeData | undefined>(undefined);
  const [helperTextPhone, setHelperTextPhone] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const addEmployee = useCallback(() => {
    if (postData) {
      postEmployee(branchId, postData)
        .then((response) => response.ok ? response.json() : undefined)
        .then((json) => {
          if (json) {
            setEmployees(employees.concat([json]));
            handleClose();
          }
        });
    }
  }, [postEmployee, postData, branchId]);

  const updateField = (field: string, data: string) => {
    let copy: EmployeeData = postData ? { ...postData } :
      {
        name: "",
        surname: "",
        patronymic: "",
        passport: "",
        phone: "",
        city: "",
        employment_date: "",  //2022-12-11T12:43
        salary: -1,
        role: ""
      };

    if (["passport", "role", "phone", "name", "employment_date",
      "city", "salary", "surname", "patronymic"].indexOf(field) >= 0) {
      // @ts-ignore
      copy[field] = data.length ? data : undefined;
    }
    setPostData(copy);
  };

  return (
    <BootstrapDialog
      onClose={handleClose}
      aria-labelledby="customized-dialog-title"
      open={isOpen}
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Add new employee to branch
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <TextField
          required
          margin="dense"
          id="surname"
          label="Surname"
          fullWidth
          onChange={(val) => {
            if (regexLetters.test(val.target.value))
              updateField("surname", val.target.value);
            else alert("Surname must contain only letters");
          }
          }
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="name"
          label="Name"
          fullWidth
          onChange={(val) => {
            if (regexLetters.test(val.target.value))
              updateField("name", val.target.value);
            else alert("Name must contain only letters");
          }}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="patronymic"
          label="Patronymic"
          fullWidth
          onChange={(val) => {
            if (regexLetters.test(val.target.value))
              updateField("patronymic", val.target.value);
            else alert("Patronymic must contain only letters");
          }
          }
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="city"
          label="City"
          fullWidth
          onChange={(val) => {
            if (regexLetters.test(val.target.value))
              updateField("city", val.target.value);
            else alert("City must contain only letters");
          }
          }
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="role"
          label="Role"
          fullWidth
          onChange={(val) => {
            if (!regexPhone.test(val.target.value)) {
              setHelperTextPhone("Phone format should be: +79998887766")
            } else {
              setHelperTextPhone("");
              updateField("role", val.target.value)
            }
          }
          }
          variant="standard"
          helperText={helperTextPhone}
        />
        <TextField
          required
          margin="dense"
          id="passport"
          label="Passport"
          fullWidth
          onChange={(val) =>
            updateField("passport", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="phone"
          label="Phone"
          placeholder="+79997775566"
          fullWidth
          onChange={(val) => {
            updateField("phone", val.target.value);
          }
          }
          variant="standard"
        />
        <label style={{ marginTop: "5px" }} htmlFor={"employment-date"}>
          Employment date
        </label>
        <input
          required
          style={{ width: "100%" }}
          type="datetime-local"
          id="employment_date"
          placeholder="dd/mm/yyyy"
          min="2010-01-01T00:00"
          max="2023-12-31T00:00"
          onChange={(val) => {
            updateField("employment_date", toServerDateFormat(val.target.value));
          }
          }
        />
        <TextField
          required
          type="number"
          margin="dense"
          id="salary"
          label="Salary"
          fullWidth
          onChange={(val) =>
            updateField("salary", val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button
          disabled={checkObjOnDefault(postData)
            || !regexPhone.test(postData?.phone!)}
          autoFocus onClick={addEmployee}>
          Add
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
};