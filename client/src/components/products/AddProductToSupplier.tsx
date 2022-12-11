import * as React from "react";
import { useState } from "react";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplier";
import { postProduct } from "../../api/supplier";

interface SupplierProductProps {
  isOpen: boolean,
  setOpen: (action: boolean) => void,
  supplierId: string,
  products: any[],
  setProducts: (list: any[]) => void
}

export function AddProductToSupplier(props: SupplierProductProps) {

  const { isOpen, setOpen, supplierId, products, setProducts } = props;
  const [price, setPrice] = useState(-1);
  const [name, setName] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const addProduct = () => {
    postProduct(supplierId, name, price)
      .then(async (response) => {
        if (response.ok) {
          alert("Product was successfully added!");
          return response.json();
        }
        else {
          const res = await response.text();
          alert(JSON.parse(res).message);
          return undefined;
        }
      })
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
          label="Product's name"
          fullWidth
          onChange={(val) =>
            setName(val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price"
          label="Product's price"
          fullWidth
          onChange={(val) => {
            if (Number(val.target.value) < 0) {
              alert("Price must be positive number!");
            }
            else
            setPrice(Number(val.target.value))
          }}
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
