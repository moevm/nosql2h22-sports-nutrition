import * as React from "react";
import { useCallback, useState } from "react";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplierDialog";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { EmployeeData, postEmployee } from "../../api/employee";

export const AddEmployee = ({ isOpen, setOpen, branchId, employees, setEmployees }: {
                              isOpen: boolean,
                              setOpen: (action: boolean) => void,
                              branchId: string,
                              employees: any[],
                              setEmployees: (list: any[]) => void
                            }
) => {

  const [postData, setPostData] = useState<EmployeeData | undefined>(undefined);

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
        employment_date: "",
        salary: 0,
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
        Add new stock to branch
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <TextField
          required
          margin="dense"
          id="name"
          label="Name"
          fullWidth
          onChange={(val) =>
            updateField("name", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="patronymic"
          label="Patronymic"
          fullWidth
          onChange={(val) =>
            updateField("patronymic", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="surname"
          label="Surname"
          fullWidth
          onChange={(val) =>
            updateField("surname", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="city"
          label="City"
          fullWidth
          onChange={(val) =>
            updateField("city", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          margin="dense"
          id="role"
          label="Role"
          fullWidth
          onChange={(val) =>
            updateField("role", val.target.value)}
          variant="standard"
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
          fullWidth
          onChange={(val) =>
            updateField("phone", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          type="datetime-local"
          margin="dense"
          id="employment_date"
          label="Employment Date"
          fullWidth
          onChange={(val) =>
            updateField("employment_date", val.target.value)}
          variant="standard"
        />
        <TextField
          required
          type="number"
          margin="dense"
          id="price"
          label="Enter amount"
          fullWidth
          onChange={(val) =>
            updateField("price", val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={addEmployee}>
          Add
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
};