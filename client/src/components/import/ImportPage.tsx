import * as React from "react";
import { useCallback, useState } from "react";
import { BootstrapDialog, BootstrapDialogTitle } from "../suppliers/FindSupplierDialog";
import DialogContent from "@mui/material/DialogContent";
import { Stack, TextField } from "@mui/material";
import DialogActions from "@mui/material/DialogActions";
import Button from "@mui/material/Button";

export const ImportPage = ({
                             isOpen, setOpen, requestFunc, setData, setLastPage,
                             lastPage, currentPage, getPageApi,
                             dataList, pageSize
                           }: {
  isOpen: boolean;
  setOpen: (action: boolean) => void;
  requestFunc: (obj: any) => Promise<Response>;
  setData: (list: any[]) => void;
  setLastPage: (flag: boolean) => void;
  lastPage: boolean;
  currentPage: number;
  dataList: any[];
  pageSize: number;
  getPageApi: (pageSize: number, pageNumber: number) => Promise<Response>;
}) => {

  const [fileData, setFileData] = useState<string | ArrayBuffer | null>(null);

  const clickToExport = useCallback(() => {
    if (fileData) {
      requestFunc(fileData).then((res) => {
        console.log("Response status: ", res.statusText);
        return res.ok ? res.json() : undefined;
      })
        .then((json) => {
          if (json) {
            if (lastPage && dataList.length + json.result.length > pageSize) {
              setLastPage(false);
            } else if (lastPage) {
              getPageApi(pageSize, currentPage)
                .then((response) => response.json())
                .then((json) => {
                  if (json.items.length) {
                    setData(json.items);
                    setLastPage(json.items.length < pageSize);
                  }
                });
            }
            handleClose();
          }
        });
    }
  }, [fileData, lastPage, setLastPage, setData,
    getPageApi, pageSize, currentPage, requestFunc, dataList]);

  const handleClose = () => setOpen(false);

  return (
    <BootstrapDialog
      onClose={handleClose}
      open={isOpen}
    >
      <BootstrapDialogTitle id="customized-dialog-title" onClose={handleClose}>
        Import data
      </BootstrapDialogTitle>
      <DialogContent dividers>
        <Stack>
          <TextField
            required
            type="file"
            margin="dense"
            id="file"
            inputProps={{
              accept: ".json"
            }}
            label="File with json data"
            onChange={() => {
              // @ts-ignore
              const file = document.getElementById("file").files[0];
              const reader = new FileReader();
              // @ts-ignore
              reader.readAsText(file);

              reader.onload = async function() {
                setFileData(reader.result);
              };

              reader.onerror = function() {
                console.log("File reader exception: ", reader.error);
              };
            }
            }
            variant="standard"
          />
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button autoFocus onClick={clickToExport}
                disabled={!fileData}>
          Find
        </Button>
      </DialogActions>
    </BootstrapDialog>
  );
};