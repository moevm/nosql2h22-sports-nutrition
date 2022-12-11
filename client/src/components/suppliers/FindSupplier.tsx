import * as React from "react";
import {useCallback, useState} from "react";
import Button from "@mui/material/Button";
import {styled} from "@mui/material/styles";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import {Box, TextField, Typography} from "@mui/material";
import "../dialog.scss";
import {isObjEmpty} from "../../api/branch";
import {FilterSupplierCriteria, getSupplier} from "../../api/supplier";
import {updateField} from "./util";
import {SuppliersTable} from "./SuppliersTable";

export const BootstrapDialog = styled(Dialog)(({ theme }) => ({
  "& .MuiDialogContent-root": {
    padding: theme.spacing(4)
  },
  "& .MuiDialogActions-root": {
    padding: theme.spacing(2)
  }
}));

export interface DialogTitleProps {
  id: string;
  children?: React.ReactNode;
  onClose: () => void;
}

export function BootstrapDialogTitle(props: DialogTitleProps) {
  const { children, onClose, ...other } = props;

  return (
    <DialogTitle sx={{ m: 2, p: 2 }} {...other}>
      {children}
      {onClose ? (
        <IconButton
          aria-label="close"
          onClick={onClose}
          sx={{
            position: "absolute",
            right: 12,
            top: 8,
            color: (theme) => theme.palette.grey[500]
          }}
        >
          <CloseIcon />
        </IconButton>
      ) : null}
    </DialogTitle>
  );
}

export function FindSupplier() {

  const [value, setValue] = useState<FilterSupplierCriteria>({});

  const [suppliers, setSuppliers] = useState([]);
  const [error, setError] = useState("");

  const findSuppliers = useCallback(() => {
    getSupplier(value)
      .then(async (response) => {
       if (response.ok) return response.json();
       else {
         const text = await response.text();
         setError(JSON.parse(text).message);
         setSuppliers([]);
         return undefined;
       }}
      )
      .then((json) => {
        if (json) {
          setError( "" );
          setSuppliers( json.result);
        }
      })
      .catch((e) => {
          setError(e.message);
          setSuppliers([]);
        }
      );
  }, [value, getSupplier]);

  return (
    <Box style={{ width: "70%" }}>
      <Typography component="div" variant="h5">
        Find supplier form
      </Typography>
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
          label="Name"
          fullWidth
          onChange={(val) =>
            updateField("name", val.target.value, value, setValue)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="email"
          label="Email"
          placeholder="supplier@gmail.com"
          fullWidth
          onChange={(val) =>
            updateField("email", val.target.value, value, setValue)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="phone"
          label="Phone"
          fullWidth
          placeholder="79998887788"
          onChange={(val) =>
            updateField("phone", val.target.value, value, setValue)}
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
        <TextField
          margin="dense"
          id="product_names"
          label="Product names"
          fullWidth
          placeholder="name1, name2"
          onChange={(val) =>
            updateField("product_names", val.target.value, value, setValue)}
          variant="standard"
          helperText={`Use "," between names of products. Example: "name1, name2"`}
        />
        <TextField
          margin="dense"
          id="product_ids"
          label="Product ids"
          fullWidth
          placeholder="id1, id2"
          onChange={(val) =>
            updateField("product_ids", val.target.value, value, setValue)}
          variant="standard"
          helperText={`Use "," between names of products. Example: id1, id2"`}
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus disabled={isObjEmpty(value)} onClick={findSuppliers}>
          Find
        </Button>
      </DialogActions>
      {error.length ? <Typography> ERROR: {error}</Typography> : null}
      {suppliers.length ? <SuppliersTable suppliers={suppliers} pagination={false} /> : null}
    </Box>
  );
}
