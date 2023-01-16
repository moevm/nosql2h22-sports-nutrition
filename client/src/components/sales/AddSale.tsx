import {Box, Button, Stack, TextField} from "@mui/material";
import * as React from "react";
import {useCallback, useState} from "react";
import {useNavigate} from "react-router-dom";
import {postSale} from "../../api/sale";
import {checkOnError} from "../../api/functions";

export interface IAddBranchResponse {
  id: string;
  name: string;
  city: string;
  employees: any[];
  stocks: any[];
}

const convertToObject = (json: any): IAddBranchResponse => {
  return {
    id: json._id,
    name: json.name,
    city: json.city,
    employees: [],
    stocks: []
  };
};

export const AddSale = () => {
  const navigate = useNavigate();
  const [branchId, setBranchId] = useState("");
  const [productId, setProductId] = useState("");
  const [supplierId, setSupplierId] = useState("");
  const [price, setPrice] = useState("");
  const [amount, setAmount] = useState("");

  const doRequest = useCallback((branchIdReq: string, productIdReq: string, supplierIdReq: string, priceReq: string, amountReq: string) => {
    postSale(branchIdReq, productIdReq, supplierIdReq, priceReq, amountReq)
      .then((response) =>
          checkOnError(response, "Sale was successfully added!"))
      .catch((e) => alert(`Error occurred: ${e.message}`));
  }, [postSale, convertToObject]);


  return (
    <Box style={{ width: "60%" }}>
      <Stack spacing={2}>
        <h2> Add new sale </h2>
        <TextField
          style={{ width: "80%" }}
          label="Branch id"
          variant="standard"
          required
          onChange={(e) => setBranchId(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Product id"
          variant="standard"
          required
          onChange={(e) => setProductId(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Supplier id"
          variant="standard"
          required
          onChange={(e) => setSupplierId(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Price"
          variant="standard"
          required
          onChange={(e) => setPrice(e.target.value)}
        />
        <TextField
          style={{ width: "80%" }}
          label="Amount"
          variant="standard"
          required
          onChange={(e) => setAmount(e.target.value)}
        />
        <Box style={{ marginLeft: "35%" }} flexDirection="row">
          <Button onClick={() => doRequest(branchId, productId, supplierId, price, amount)}
                  disabled={!branchId.length || !productId.length || !supplierId.length || !amount.length || !price.length}>
            Add
          </Button>
          <Button onClick={() => navigate("/sales")}>
            Cancel
          </Button>
        </Box>
      </Stack>
    </Box>
  );
};
