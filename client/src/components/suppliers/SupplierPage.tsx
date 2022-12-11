import * as React from "react";
import { useEffect, useState } from "react";
import { Box, Button, Stack, Tab, Tabs, TextField, Typography } from "@mui/material";
import { useParams } from "react-router-dom";
import { NotFound } from "../NotFound";
import { getSupplierById } from "../../api/supplier";
import { ProductsList } from "../products/ProductsList";
import { AddProductToSupplier } from "../products/AddProductToSupplier";
import { TabPanel } from "../tabs/tabs";
import { isObjEmpty } from "../../api/branch";
import { FilterProductCriteria, getProductsOfSupplier } from "../../api/product";
import { ProductsDialog } from "../products/ProductsDialog";

export const SupplierPage = () => {
  const params = useParams();
  const [supplier, setSupplier] = useState<any>(undefined);
  const [products, setProducts] = useState<any[]>([]);
  const [isOpenForm, setOpenForm] = useState(false);

  const [tabValue, setTabValue] = useState(0);
  const [productsFilterCriteria, setProductsFilterCriteria] = useState<FilterProductCriteria>({});

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  useEffect(() => {
    getSupplierById(params.id!)
      .then((response) => response.json())
      .then((json) => {
        setSupplier(json.result[0]);
        setProducts(json.result[0].products);
      });
  }, [params, getSupplierById]);

  useEffect(() => {
    if (!supplier || isObjEmpty(productsFilterCriteria)) {
      return;
    }
    getProductsOfSupplier(productsFilterCriteria, supplier._id)
      .then((response) => response.json())
      .then((json) => {
        setProducts(json.result);
      })
      .catch((err) => setProducts([]));
  }, [getProductsOfSupplier, productsFilterCriteria]);

  if (!supplier) {
    return <NotFound />;
  }
  return (
    <Stack spacing={2}>
      <Typography variant={"h4"}> Supplier {supplier.name} </Typography>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="Info"
          />
          <Tab
            label="Products"
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
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
      </TabPanel>

      <TabPanel value={tabValue} index={1}>
        <Typography component="span" variant={"h5"}> Products of supplier </Typography>
        <Box sx={{ flexDirection: "row" }}>
          <Button onClick={() => setOpenForm(!isOpenForm)}>
            Add new product
          </Button>
        </Box>
        <AddProductToSupplier isOpen={isOpenForm} setOpen={setOpenForm} supplierId={supplier._id}
                              products={products} setProducts={setProducts} />
        <ProductsDialog onChange={setProductsFilterCriteria} value={productsFilterCriteria} />
        <ProductsList products={products} />
      </TabPanel>
    </Stack>
  );
};
