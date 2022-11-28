import { useState } from "react";
import { postStock } from "../../api/branch";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplierDialog";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import * as React from "react";

export const AddEmployee = ({ isOpen, setOpen, branchId, employees, setEmployees }: {
                                     isOpen: boolean,
                                     setOpen: (action: boolean) => void,
                                     branchId: string,
                                     employees: any[],
                                     setEmployees: (list: any[]) => void
                                   }
  ) => {

    const [price, setPrice] = useState(-1);
    const [amount, setAmount] = useState(-1);
    const [productId, setProductId] = useState("");

    const handleClose = () => {
      setOpen(false);
    };

    const addProduct = () => {
      postStock(branchId, productId, price, amount)
        .then((response) => response.ok ? response.json() : undefined)
        .then((json) => {
          if (json) {
            setEmployees(employees.concat([json]));
            handleClose();
          }
        });
    }

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
            autoFocus
            margin="dense"
            id="name"
            label="Enter product's id"
            fullWidth
            onChange={(val) =>
              setProductId(val.target.value)}
            variant="standard"
          />
          <TextField
            type="number"
            margin="dense"
            id="price"
            label="Enter price"
            fullWidth
            onChange={(val) =>
              setPrice(Number(val.target.value))}
            variant="standard"
          />
          <TextField
            type="number"
            margin="dense"
            id="price"
            label="Enter amount"
            fullWidth
            onChange={(val) =>
              setAmount(Number(val.target.value))}
            variant="standard"
          />
        </DialogContent>
        <DialogActions>
          <Button autoFocus onClick={addProduct}
                  disabled={!productId.length || price < 0 || amount < 0}>
            Add
          </Button>
        </DialogActions>
      </BootstrapDialog>
    );
  }
}