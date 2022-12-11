import * as React from "react";
import { useCallback, useEffect, useState } from "react";
import Button from "@mui/material/Button";
import { styled } from "@mui/material/styles";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import { Box, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "../dialog.scss";
import { FilterEmployeesCriteria, isObjEmpty } from "../../api/branch";
import { FilterSupplierCriteria, getSupplier } from "../../api/supplier";
import { updateField } from "./util";
import { findEmployee, findEmployeesInBranch } from "../../api/employee";
import { EmployeesList } from "../employees/EmployeesList";
import { SuppliersList } from "./SuppliersList";
import { SuppliersTable } from "./SuppliersTable";

export const BootstrapDialog = styled(Dialog)(({ theme }) => ({
  "& .MuiDialogContent-root": {
    padding: theme.spacing(4)
  },
  "& .MuiDialogActions-root": {
    padding: theme.spacing(2)
  }
}));

export interface DialogTitleProps {
  id: string;
  children?: React.ReactNode;
  onClose: () => void;
}

export function BootstrapDialogTitle(props: DialogTitleProps) {
  const { children, onClose, ...other } = props;

  return (
    <DialogTitle sx={{ m: 2, p: 2 }} {...other}>
      {children}
      {onClose ? (
        <IconButton
          aria-label="close"
          onClick={onClose}
          sx={{
            position: "absolute",
            right: 12,
            top: 8,
            color: (theme) => theme.palette.grey[500]
          }}
        >
          <CloseIcon />
        </IconButton>
      ) : null}
    </DialogTitle>
  );
}

interface FindSupplierProps {
  onChange: (val: FilterSupplierCriteria) => void,
  value: FilterSupplierCriteria
}

const SUPPLIERS_NOT_FOUND = "Suppliers not found";

export function FindSupplier() {

  const [value, setValue] = useState<FilterSupplierCriteria>({});

  const [suppliers, setSuppliers] = useState([]);
  const [error, setError] = useState("");

  const findSuppliers = useCallback(() => {
    getSupplier(value)
      .then((response) => response.ok ? response.json() : undefined)
      .then((json) => {
        setError(json ? "" : SUPPLIERS_NOT_FOUND)
        setSuppliers(json ? json.result : undefined);
      })
      .catch((e) => {
          setError(e.message + ". " + SUPPLIERS_NOT_FOUND);
          setSuppliers([]);
        }
      );
  }, [value, getSupplier]);

  // const findSupplier = () => {
  //   navigate("/supplier/" + value,
  //     { replace: true });
  // };

  return (
    <Box style={{width: "70%"}}>
      <Typography component="div" variant="h5">
        Find supplier form
      </Typography>
      <DialogContent dividers>
        <TextField
          autoFocus
          margin="dense"
          id="name"
          label="Id"
          fullWidth
          onChange={(val) =>
            updateField("_id", val.target.value, value, setValue)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Name"
          fullWidth
          onChange={(val) =>
            updateField("name", val.target.value, value, setValue)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Email"
          fullWidth
          onChange={(val) =>
            updateField("email", val.target.value, value, setValue)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Phone"
          fullWidth
          onChange={(val) =>
            updateField("phone", val.target.value, value, setValue)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus disabled={isObjEmpty(value)} onClick={findSuppliers} >
          Find
        </Button>
      </DialogActions>
      {error.length ? <Typography> ERROR: {error}</Typography> : null}
      {suppliers.length ? <SuppliersTable suppliers={suppliers} pagination={false} /> : null}
    </Box>
  );
}
