import * as React from "react";
import { useEffect, useState } from "react";
import { Stack, TextField } from "@mui/material";
import { useParams } from "react-router-dom";
import { NotFound } from "../NotFound";
import { getSupplier } from "../../api/supplier";

export const SupplierPage = () => {
  const params = useParams();
  const [supplier, setSupplier] = useState<any>(undefined);
  useEffect(() => {
    getSupplier(params.id!)
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
          readOnly: true
        }}
        value={supplier._id}
      />
      <TextField
        style={{ width: "80%" }}
        id="outlined-basic"
        label="Name"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={supplier.name}
      />
      <TextField
        style={{ width: "80%" }}
        id="filled-basic"
        label="Phone"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={supplier.phone}
      />
      <TextField
        style={{ width: "80%" }}
        id="filled-basic"
        label="City"
        variant="outlined"
        InputProps={{
          readOnly: true
        }}
        value={supplier.email}
      />
    </Stack>
  );
};
