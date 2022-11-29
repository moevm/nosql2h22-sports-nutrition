import * as React from "react";
import { useEffect, useState } from "react";
import { IconButton, Stack, TextField, Typography } from "@mui/material";
import { useParams } from "react-router-dom";
import { NotFound } from "../NotFound";
import { getSupplier } from "../../api/supplier";
import { ProductsList } from "../products/ProductsList";
import { AddProductToSupplier } from "../products/AddProductToSupplier";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";

export const SupplierPage = () => {
  const params = useParams();
  const [supplier, setSupplier] = useState<any>(undefined);
  const [products, setProducts] = useState<any[]>([]);
  const [isOpenForm, setOpenForm] = useState(false);

  useEffect(() => {
    getSupplier(params.id!)
      .then((response) => response.json())
      .then((json) => {
        setSupplier(json);
        setProducts(json.products);
      });
  }, [params, getSupplier]);

  if (!supplier) {
    return <NotFound />;
  }
  return (
    <Stack spacing={2}>
      <Typography variant={"h4"}> Supplier {supplier.name} </Typography>
      <TextField
        style={{ width: "80%" }}
        label="Id"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={supplier._id}
      />
      <TextField
        style={{ width: "80%" }}
        label="Name"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={supplier.name}
      />
      <TextField
        style={{ width: "80%" }}
        label="Phone"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={supplier.phone}
      />
      <TextField
        style={{ width: "80%" }}
        label="City"
        variant="standard"
        InputProps={{
          readOnly: true
        }}
        value={supplier.email}
      />
      <Typography variant={"h5"}> Products of supplier </Typography>
      <IconButton color="inherit" title="Add new product"
                  style={{ width: "2em" }}
                  onClick={() => setOpenForm(!isOpenForm)}>
        <AddCircleOutlineIcon />
      </IconButton>
      <AddProductToSupplier isOpen={isOpenForm} setOpen={setOpenForm} supplierId={supplier._id}
                            products={products} setProducts={setProducts} />
      <ProductsList products={products} />
    </Stack>
  );
};
