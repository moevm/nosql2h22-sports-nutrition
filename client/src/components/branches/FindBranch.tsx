import { useNavigate } from "react-router-dom";
import * as React from "react";
import { useState } from "react";
import DialogContent from "@mui/material/DialogContent";
import { Box, TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import "../dialog.scss";
import { BootstrapDialogTitle } from "../suppliers/FindSupplier";

const makeQueryString = (query: string, arg: string) => {
  if (arg.length) {
    query += query.length ? `/${arg}` : arg;
  } else {
    query += query.length ? "/ " : " ";
  }
  return query;
};

export function FindBranch({ setOpen }: {
                                   setOpen: (action: boolean) => void
                                 }
) {

  const navigate = useNavigate();
  const [id, setId] = useState("");
  const [name, setName] = useState("");
  const [city, setCity] = useState("");

  const handleClose = () => {
    setOpen(false);
  };

  const findBranches = () => {
    let query = "";
    query += city.length ? city : " ";
    query = makeQueryString(query, name);
    query = makeQueryString(query, id);
    navigate(`/branch/${query}`,
      { replace: true });
  };

  return (
    <Box width="70%">
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Find branch form
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <TextField
          margin="dense"
          id="id"
          label="Enter branch's id"
          fullWidth
          onChange={(val) =>
            setId(val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="name"
          label="Enter branch's name"
          fullWidth
          onChange={(val) =>
            setName(val.target.value)}
          variant="standard"
        />
        <TextField
          margin="dense"
          id="city"
          label="Enter branch's city"
          fullWidth
          onChange={(val) =>
            setCity(val.target.value)}
          variant="standard"
        />
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={findBranches}
                disabled={!id.length && !name.length && !city.length}>
          Find
        </Button>
      </DialogActions>
    </Box>
  );
}
