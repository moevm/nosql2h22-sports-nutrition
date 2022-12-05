import * as React from "react";
import { useState } from "react";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplierDialog";
import { postProduct } from "../../api/supplier";

export function AddProductToSupplier({ isOpen, setOpen, supplierId, products, setProducts }: {
                                       isOpen: boolean,
                                       setOpen: (action: boolean) => void,
                                       supplierId: string,
                                       products: any[],
                                       setProducts: (list: any[]) => void
                                     }
) {

  const [price, setPrice] = useState(-1);
  const [name, setName] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const addProduct = () => {
    postProduct(supplierId, name, price)
      .then((response) => response.ok ? response.json() : undefined)
      .then((json) => {
        if (json) {
          setProducts(products.concat([json]));
          handleClose();
        }
      });
  };

  return (
    <BootstrapDialog
      onClose={handleClose}
      aria-labelledby="customized-dialog-title"
      open={isOpen}
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Add new product to supplier
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <TextField
          autoFocus
          margin="dense"
          id="name"
          label="Enter product's name"
          fullWidth
          onChange={(val) =>
            setName(val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price"
          label="Enter product's price"
          fullWidth
          onChange={(val) =>
            setPrice(Number(val.target.value))}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={addProduct}
                disabled={!name.length || price < 0}>
          Add
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
}
