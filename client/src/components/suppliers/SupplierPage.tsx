import * as React from "react";
import { useEffect, useState } from "react";
import { IconButton, Stack, TextField } from "@mui/material";
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
      <h2> Supplier {supplier.name} </h2>
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
      <h2> Products of supplier </h2>
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
