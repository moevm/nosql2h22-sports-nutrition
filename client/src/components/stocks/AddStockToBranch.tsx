import * as React from "react";
import { useState } from "react";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplier";
import DialogContent from "@mui/material/DialogContent";
import { TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { postStock } from "../../api/branch";
import { checkObjOnNegativeNumbers } from "../../api/functions";

const errorMessageId = "Error in entered product's id. Product doesn't exist";

interface StockToBranchProps {
  isOpen: boolean,
  setOpen: (action: boolean) => void,
  branchId: string,
  stocks: any[],
  setStocks: (list: any[]) => void
}
export function AddStockToBranch(props: StockToBranchProps) {
  const { isOpen, setOpen, branchId, stocks, setStocks } = props;
  const [price, setPrice] = useState(-1);
  const [amount, setAmount] = useState(-1);
  const [productId, setProductId] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const addProduct = () => {
    postStock(branchId, productId, price, amount)
      .then((response) => response.ok ? response.json() : undefined)
      .then((json) => {
        if (json) {
          setErrorMessage("");
          setStocks(stocks.concat([json]));
          handleClose();
        }
        else {
          setErrorMessage(errorMessageId);
        }
      })
      .catch((error) => setErrorMessage(errorMessageId));
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
        {errorMessage}
        <TextField
          autoFocus
          margin="dense"
          id="name"
          label="Product's id"
          fullWidth
          onChange={(val) =>
            setProductId(val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price"
          label="Price"
          fullWidth
          onChange={(val) => {
            if (Number(val.target.value) < 0) {
              alert("Price must be not negative");
              return;
            }
            setPrice(Number(val.target.value))
          }
          }
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price"
          label="Amount"
          fullWidth
          onChange={(val) => {
            if (Number(val.target.value) < 0) {
              alert("Amount must be not negative");
              return;
            }
            setAmount(Number(val.target.value))
          }
          }
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={
          addProduct}
                disabled={!productId.length || price < 0 || amount < 0}>
          Add
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
}
