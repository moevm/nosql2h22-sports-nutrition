import * as React from "react";
import { useCallback, useState } from "react";
import { isObjEmpty } from "../../api/branch";
import { Box, Typography } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import { FilterProductCriteria, getProducts } from "../../api/product";
import { FindProductsContent } from "./FindProductsContent";
import { updateField } from "./util";
import { ProductsList } from "./ProductsList";

export function FindProductsEverywhere() {

  const [curValue, setCurValue] = useState<FilterProductCriteria>({});

  const [products, setProducts] = useState([]);
  const [error, setError] = useState("");

  const findProducts = useCallback(() => {
    getProducts(curValue)
      .then(async (response) => {
        if (response.ok) return response.json();
        else {
          const text = await response.text();
          setError(JSON.parse(text).message);
          setProducts([]);
          return undefined;
        }
      })
      .then((json) => {
        if (json) {
          setError("");
          setProducts(json.result);
        }
      })
      .catch((e) => {
          setError(e.message);
          setProducts([]);
        }
      );
  }, [curValue, getProducts]);

  return (
    <Box>
      <Box width="70%">
        <Typography variant="h5">
          Find products among all suppliers
        </Typography>
        <FindProductsContent updateField={updateField} value={curValue} setValue={setCurValue} />
        <DialogActions>
          <Button autoFocus onClick={findProducts}
                  disabled={isObjEmpty(curValue) ||
                    Number(curValue.price_from) > Number(curValue.price_to)}>
            Find
          </Button>
        </DialogActions>
      </Box>
      {error.length ? <Typography> ERROR: {error}</Typography> : null}
      {products.length ? <ProductsList products={products} ofAllSuppliers={true} /> : null}
    </Box>
  );
}
