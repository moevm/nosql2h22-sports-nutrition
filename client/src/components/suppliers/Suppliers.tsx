import * as React from "react";
import { useState } from "react";
import { Box, Tab, Tabs } from "@mui/material";
import { SuppliersList } from "./SuppliersList";
import { FindSupplierDialog } from "./FindSupplierDialog";
import { TabPanel } from "../tabs";
import { AddSupplier } from "./AddSupplier";

export const Suppliers = () => {
  const [isOpenForm, setOpenForm] = useState(false);
  const [tabValue, setTabValue] = useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
  };

  return (
    <Box>
      <h1> Suppliers page </h1>
      <Box flexDirection={"row"}>
        <Tabs value={tabValue} onChange={handleChange}>
          <Tab
            label="Suppliers list"
          />
          <Tab
            label="Add new supplier"
          />
          <Tab
            label="Find supplier by id"
            onClick={() => setOpenForm(!isOpenForm)}
          />
        </Tabs>
      </Box>
      <TabPanel value={tabValue} index={0}>
        <SuppliersList />
      </TabPanel>
      <TabPanel value={tabValue} index={1}>
        <AddSupplier />
      </TabPanel>
      <TabPanel value={tabValue} index={2}>
        <FindSupplierDialog isOpen={isOpenForm} setOpen={setOpenForm} />
      </TabPanel>
    </Box>
  );
};
