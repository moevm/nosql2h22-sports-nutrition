import * as React from "react";
import { useEffect, useState } from "react";
import DialogContent from "@mui/material/DialogContent";
import { Box, IconButton, TextField, Typography } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import SearchOutlinedIcon from "@mui/icons-material/SearchOutlined";
import { FilterStocksCriteria, isObjEmpty } from "api/branch";
import { checkObjOnNegativeNumbers } from "../../api/functions";

export function FindStockDialog({ onChange, value }: {
                                  onChange: (val: FilterStocksCriteria) => void,
                                  value: FilterStocksCriteria
                                }
) {

  const [curValue, setCurValue] = useState<FilterStocksCriteria>(value);

  useEffect(() => {
    setCurValue(value);
  }, [value]);

  const updateField = (field: string, data: string) => {
    const copy: FilterStocksCriteria = { ...curValue };
    if (["_id", "supplier_id", "product_id", "name",
      "amount_from", "amount_to", "price_from", "price_to"].indexOf(field) >= 0) {
      // @ts-ignore
      copy[field] = data.length ? data : undefined;
    }
    setCurValue(copy);
  };

  return (
    <Box sx={{ width: "60%" }}>
      <Typography variant="h5">
        Stocks
      </Typography>
      <DialogContent dividers>
        <TextField
          margin="dense"
          id="id"
          label="Stock id"
          fullWidth
          onChange={(val) =>
            updateField("_id", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="supplier"
          label="Supplier id"
          fullWidth
          onChange={(val) =>
            updateField("supplier_id", val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="product"
          label="Product id"
          fullWidth
          onChange={(val) =>
            updateField("product_id", val.target.value)}
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
          type="number"
          margin="dense"
          id="amount_from"
          label="Amount from"
          fullWidth
          onChange={(val) =>
            updateField("amount_from", val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="amount_to"
          label="Amount to"
          fullWidth
          onChange={(val) =>
            updateField("amount_to", val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price_from"
          label="Price from"
          fullWidth
          onChange={(val) =>
            updateField("price_from", val.target.value)}
          variant="standard"
        />
        <TextField
          type="number"
          margin="dense"
          id="price_to"
          label="Price to"
          fullWidth
          onChange={(val) =>
            updateField("price_to", val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <IconButton
          onClick={() => {
            if (checkObjOnNegativeNumbers(curValue)) {
              alert("Amount and price must be not negative");
              return;
            }
            if (Number(curValue.amount_from) > Number(curValue.amount_to)) {
              alert("Amount from must be less then amount to");
              return;
            }
            if (Number(curValue.price_from) > Number(curValue.price_to)) {
              alert("Price from must be less then price to");
              return;
            }
            onChange(curValue);
          }
          }
          disabled={isObjEmpty(curValue)}
          color="inherit" title="Find stocks"
          style={{ width: "2em", margin: "10px" }}>
          <SearchOutlinedIcon />
        </IconButton>
      </DialogActions>
    </Box>
  );
}