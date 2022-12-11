import {TextField} from "@mui/material";
import DialogContent from "@mui/material/DialogContent";
import * as React from "react";
import {FilterProductCriteria} from "../../api/product";


interface FindProductsContentProps {
  updateField: (name: string, value: string, curValue: FilterProductCriteria,
                setCurValue: (val: FilterProductCriteria) => void) => void;
  value: FilterProductCriteria;
  setValue: (val: FilterProductCriteria) => void;
  oneSupplier?: boolean;
}

export const FindProductsContent = (props: FindProductsContentProps) => {
  const { updateField, value, setValue, oneSupplier } = props;
  return (
    <DialogContent dividers>
      <TextField
        autoFocus
        margin="dense"
        id="id"
        label="Id"
        fullWidth
        onChange={(val) =>
          updateField("_id", val.target.value, value, setValue)}
        variant="standard"
      />
      <TextField
        margin="dense"
        id="name"
        label="Names"
        fullWidth
        onChange={(val) =>
          updateField("names", val.target.value, value, setValue)}
        variant="standard"
        helperText={`Use "," between names. Example: "name1, name2"`}
      />
      <TextField
        margin="dense"
        type="number"
        id="price_from"
        label="Price from"
        fullWidth
        onChange={(val) =>
          updateField("price_from", val.target.value, value, setValue)}
        variant="standard"
      />
      <TextField
        margin="dense"
        id="price_to"
        type="number"
        label="Price to"
        fullWidth
        onChange={(val) =>
          updateField("price_to", val.target.value, value, setValue)}
        variant="standard"
      />
      <TextField
        margin="dense"
        id="descriptor"
        label="Descriptor ids"
        placeholder="descriptor1, descriptor2"
        fullWidth
        onChange={(val) =>
          updateField("descriptor_ids", val.target.value, value, setValue)}
        variant="standard"
        helperText={`Use "," between descriptors. Example: "descriptor1, descriptor2"`}
      />
      {oneSupplier ? null :
        <TextField
          margin="dense"
          id="supplier_ids"
          label="Supplier ids"
          fullWidth
          placeholder="id1, id2"
          onChange={(val) =>
            updateField("supplier_ids", val.target.value, value, setValue)}
          variant="standard"
          helperText={`Use "," between ids of suppliers. Example: "id1, id2"`}
        />
      }
    </DialogContent>
  );
};