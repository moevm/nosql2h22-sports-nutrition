import * as React from "react";
import {  Stack, TextField } from "@mui/material";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { NotFound } from "../NotFound";

export const SupplierPage = () => {
  const [supplier, setSupplier] = useState<any>(undefined);
  const params = useParams();
  useEffect(() => {
    fetch(`http://localhost:8008/supplier/${params.id}`, {
      method: "GET",
      mode: "cors",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
    })
      .then((response) => response.json())
      .then((json) => {
        setSupplier(json);
      });
  }, [params]);
  if (!supplier) {
    return <NotFound />;
  }
  return (
    <Stack spacing={2}>
      <h2> Supplier {supplier.name} </h2>
      <a> Show products</a>
      <TextField
        style={{ width: "80%" }}
        id="outlined-basic"
        label="Id"
        variant="outlined"
        InputProps={{
          readOnly: true,
        }}
        value={supplier._id}
      />
      <TextField
        style={{ width: "80%" }}
        id="outlined-basic"
        label="Name"
        variant="outlined"
        InputProps={{
          readOnly: true,
        }}
        value={supplier.name}
      />
      <TextField
        style={{ width: "80%" }}
        id="filled-basic"
        label="Phone"
        variant="outlined"
        InputProps={{
          readOnly: true,
        }}
        value={supplier.phone}
      />
      <TextField
        style={{ width: "80%" }}
        id="filled-basic"
        label="City"
        variant="outlined"
        InputProps={{
          readOnly: true,
        }}
        value={supplier.email}
      />
    </Stack>
  );
};
