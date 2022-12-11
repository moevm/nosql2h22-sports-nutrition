import {isObjEmpty} from "../../api/branch";
import * as React from "react";
import {useEffect, useState} from "react";
import {Box, Button, Typography} from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import {FilterProductCriteria} from "../../api/product";
import {FindProductsContent} from "./FindProductsContent";
import {updateField} from "./util";

interface FindProductsProps {
  onChange: (val: FilterProductCriteria) => void,
  value: FilterProductCriteria
}

export function ProductsDialog({ onChange, value }: FindProductsProps) {

  const [curValue, setCurValue] = useState<FilterProductCriteria>(value);

  useEffect(() => {
    setCurValue(value);
  }, [value]);

  return (
    <Box sx={{ width: "60%" }}>
      <Typography variant="h6">
        Filter products
      </Typography>
      <FindProductsContent oneSupplier={true}
                           updateField={updateField}
                           value={curValue}
                           setValue={setCurValue} />
      <DialogActions>
        <Button
          onClick={() => onChange(curValue)}
          disabled={isObjEmpty(curValue)}>
          Find
        </Button>
      </DialogActions>
    </Box>
  );
}