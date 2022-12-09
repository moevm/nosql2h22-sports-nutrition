import * as React from "react";
import { useState } from "react";
import Button from "@mui/material/Button";
import { styled } from "@mui/material/styles";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import { TextField } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "../dialog.scss";

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

export function FindSupplier({ isOpen, setOpen }: {
                                     isOpen: boolean,
                                     setOpen: (action: boolean) => void
                                   }
) {

  const navigate = useNavigate();
  const [value, setValue] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const findSupplier = () => {
    navigate("/supplier/" + value,
      { replace: true });
  };

  return (
    <BootstrapDialog
      onClose={handleClose}
      aria-labelledby="customized-dialog-title"
      open={isOpen}
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Find supplier form
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <TextField
          autoFocus
          margin="dense"
          id="name"
          label="Enter supplier's id"
          fullWidth
          onChange={(val) =>
            setValue(val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={findSupplier}
                disabled={!value.length}>
          Find
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
}
