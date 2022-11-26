import * as React from "react";
import { useState } from "react";
import { Box, IconButton, Tab, Tabs } from "@mui/material";
import AddCircleOutlineIcon from "@mui/icons-material/AddCircleOutline";
import { Link as RouterLink } from "react-router-dom";
import { SuppliersList } from "./SuppliersList";
import { FindSupplierDialog } from "./FindSupplierDialog";

export const Suppliers = () => {
  const [isOpenForm, setOpenForm] = useState(false);

  return (
    <Box>
      <h1> Suppliers page </h1>
      <Tabs>
        <Tab
          sx={{ display: "flex", marginRight: 0, alignSelf: "end" }}
          component={RouterLink}
          to="/suppliers/add"
          value="add"
          label={
            <label key="label" title="Add new supplier">
              Add new supplier
              <IconButton color="inherit" aria-label="Add new supplier">
                <AddCircleOutlineIcon />
              </IconButton>
            </label>
          }
        />
        <Tab
          value="find"
          label="Find supplier by id"
          onClick={() => setOpenForm(!isOpenForm)}
        />
      </Tabs>
      <FindSupplierDialog isOpen={isOpenForm} setOpen={setOpenForm} />
      <SuppliersList />
    </Box>
  );
};
