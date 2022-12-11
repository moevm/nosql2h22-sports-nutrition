import DialogContent from "@mui/material/DialogContent";
import {Stack, TextField} from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";
import * as React from "react";
import {useCallback, useState} from "react";
import {BootstrapDialog, BootstrapDialogTitle} from "../suppliers/FindSupplier";

interface ExportPageProps {
  isOpen: boolean,
  setOpen: (action: boolean) => void,
  requestFunc: (a: number, b: number) => Promise<Response>;
}

export const ExportPage = ({ isOpen, setOpen, requestFunc }: ExportPageProps) => {

  const handleClose = () => setOpen(false);
  const [pageNumber, setPageNumber] = useState(0);
  const [size, setSize] = useState(0);

  const clickToExport = useCallback(() => {
    if (pageNumber < 1 || size < 1) {
      return;
    }
    requestFunc(size, pageNumber)
      .then((response) => response.json())
      .then((json) => {
        const url = window.URL.createObjectURL(
          new Blob([JSON.stringify(json, null, 4)])
        );
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute(
          "download",
          `export.json`
        );
        document.body.appendChild(link);
        link.click();
        link.parentNode!.removeChild(link);
      });
  }, [pageNumber, size]);

  return (
    <BootstrapDialog
      onClose={handleClose}
      open={isOpen}
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Export page
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <Stack>
          <TextField
            required
            type="number"
            margin="dense"
            id="page"
            label="Page number"
            onChange={(val) => {
              setPageNumber(Number(val.target.value));
            }}
            variant="standard"
          />
          <TextField
            required
            type="number"
            margin="dense"
            id="size"
            label="Amount of branches to export"
            onChange={(val) =>
              setSize(Number(val.target.value))}
            variant="standard"
          />
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={clickToExport}
                disabled={size < 1 && pageNumber < 1}>
          Export
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
};